from abc import ABC , abstractmethod
from dataclasses import dataclass , field
from typing import List, Tuple, Dict, Optional, Any
import json 
import csv
import os

#-- dataclass for pipeline metadata------
@dataclass
class PipelineResult:
    pipeline_name: str
    input_path: str
    output_path: str
    rows_loaded: int=0
    rows_after_clean: int=0
    rows_saved: int=0
    errors: List[str] = field(default_factory=list)
    success: bool= False
    
    @property
    def rows_dropped(self) -> int:
        return self.rows_loaded - self.rows_after_clean
    
    @property
    def drop_rate(self) -> float:
        if self.rows_loaded == 0 :
            return 0.0
        return self.rows_dropped / self.rows_loaded
    
    def summary(self) -> str:
        return (
            f"\n{'='*40}\n"
            f"Pipeline: {self.pipeline_name}\n"
            f"Status:{'Sucess' if self.success else 'Failed'}\n"
            f"Loaded: {self.rows_loaded} rows \n"
            f"Cleaned:  {self.rows_after_clean} rows\n"
            f"Dropped:  {self.rows_dropped} rows ({self.drop_rate:.1%})\n"
            f"Saved:    {self.rows_saved} rows\n"
            f"Errors:   {len(self.errors)}\n"
            f"{'='*40}"
        )
        
# -- Custom expections ---------------------
class PipelineError(Exception):
    """Base exception for all pipeline errors."""
    pass

class DataLoadError(PipelineError):
    """Raised when data cannot be loaded """

class DataCleanError(PipelineError):
    """Raised when data cleaning fails."""

class DataSaveError(PipelineError):
    """Raised when data cannot be saved."""
    

# --Abstract base Pipeline-----------------------
class BasePipeline(ABC):
    """
    Abstract base class for all data pipelines.
    Defines the interface every pipeline must implement.
    """
    
    def __init__(self,name:str):
        self._name = name 
        self._data : Optional[List[Dict[str,Any]]] = None
        self._result = PipelineResult(name,"","")
        
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def data(self) -> Optional[List[Dict[str,Any]]]:
        return self._data
    
    @property
    def is_loaded(self) -> bool:
        return self._data is not None
    
    @property 
    def row_count(self) -> int:
        return len(self._data) if self._data else 0
    
    @abstractmethod
    def load(self,path:str) -> List[Dict[str,Any]]:
        pass
    
    @abstractmethod
    def clean(self,data:List[Dict[str,Any]]) -> List[Dict[str,Any]]:
        pass
    
    @abstractmethod
    def save(self,data:List[Dict[str,Any]],path: str) -> bool:
        pass
    
    def run(self,input_path:str, output_path:str) -> PipelineResult:
        """ 
        Template method - runs the full pipeline in order. 
        Subclass do NOT override this - they override individual steps.
        """
        self._result = PipelineResult(self._name, input_path, output_path)
        print(f"[{self._name}] Starting pipeline...")
        
        try: 
            #Step 1: Load
            print(f"[{self._name}] Loading data from {input_path}...")
            self._data = self.load(input_path)
            self._result.rows_loaded = len(self._data) 
            print(f"[{self._name}] Loaded {self._result.rows_loaded} rows") 
            
            #Step 2: Clean
            print(f"[{self._name}] Cleaning data...")
            cleaned = self.clean(self._data)  
            self._result.rows_after_clean = len(cleaned)
            print(f"[{self._name}] After clean: {self._result.rows_after_clean} rows")
            
            #Step 3: Transform
            print(f"[{self._name}] Transforming data...")
            transformed = self.transform(cleaned)
            
            #Step 4: Save
            print(f"[{self._name}] Saving to {output_path}")
            success = self.save(transformed, output_path)
            self._result.rows_saved = len(transformed)
            self._result.success = success
            
        except PipelineError as e:
            self._result.errors.append(str(e))
            print(f"[{self._name}] Pipeline error:{e}")
        except Exception as e:
            self._result.errors.append(f"Unexpected error: {e}")
            print(f"[{self._name}] Unexpected error: {e}")
            
        print(self._result.summary())
        return self._result 
    
    @staticmethod
    def validate_path(path:str) -> bool:
        """Check if a file path exists."""
        return os.path.exists(path)
    
    @staticmethod
    def ensure_dir(path:str) -> None:
        """Create directory if it doesn't exists.""" 
        os.makedirs(os.path.dirname(path),exist_ok=True)
        
    @classmethod
    def from_config(cls,config: Dict[str,Any]) -> 'BasePipeline':
        return cls(name = config.get("name","pipeline"))
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self._name}',laoded = {self.is_loaded})"
    
    def __len__(self) -> int:
        return self.row_count
    
    
# -- Concrete CSV Pipeline ------------------------------------
class CSVPipeline(BasePipeline):
    """ 
    Concrete Pipeline that loads and saves CSV files.
    Cleans: removes empty rows, strips whitespaces.
    Transforms: normalises column names, converts types.
    """
    def __init__(self, name:str, required_columns: Optional[List[str]] = None):
        super().__init__(name)
        self.required_columns = required_columns or [] 
        
    def load(self, path:str) -> List[Dict[str, Any]]:
        if not self.validate_path(path):
            raise DataLoadError(f"File not found: {path}")
        
        try :
            with open(path,"r",newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                data = [dict(row) for row in reader]
                
            if not data :
                raise DataLoadError(f"File is empty: {path}")
            
            # Check required columns
            if self.required_columns:
                missing = [c for c in self.required_columns if c not in data[0]]
                if missing :
                    raise DataLoadError(f"Missing required columns: {missing}")
                
            return data    
        except (IOError,csv.Error) as e:
            raise DataLoadError(f"Failed to read CSV: {e}")
        
    def clean(self,data: List[Dict[str,Any]]) -> List[Dict[str,Any]]:
        cleaned = []
        for row in data:
            # Strip whitespace from all values 
            row = {k: v.strip() if isinstance(v,str) else v
                   for k,v in row.items()}
            # Remove rows where ALL values are empty
            if all(v=="" for v in row.values()):
                continue
            
            cleaned.append(row)
        return cleaned
    
    def transform(self, data: List[Dict[str,Any]]) -> List[Dict[str,Any]] :
        transformed = []
        for row in data:
            # Normalize column names: lowercase, replace spaces with underscores
            new_row = {
                k.lower().replace(" ", "_"):v for k,v in row.items()
            } 
            transformed.append(new_row)
        return transformed
    
    def save(self, data: List[Dict[str,Any]], path: str) -> bool:
        if not data:
            raise DataSaveError("No data to save")
        
        try:
            self.ensure_dir(path)
            with open(path,"w",newline="",encoding = 'utf-8') as f:
                writer = csv.DictWriter(f,fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            return True
        except IOError as e:
            raise DataSaveError(f"Failed to save CSV: {e}")
        
        
# -- Run it -------------------------------------
if __name__ == "__main__":
    # create sample CSV data to test with 
    sample_csv = "data/raw/students.csv"
    os.makedirs("data/raw",exist_ok=True)
    os.makedirs("data/processed",exist_ok=True)
    
    with open(sample_csv,"w",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Score", "City"])
        writer.writerow(["  Alice  ", "85", "Jaipur"])
        writer.writerow(["Bob", "42", "Delhi"])
        writer.writerow(["", "", ""])           # empty row — should be dropped
        writer.writerow(["Charlie", "91", "Mumbai"])
    
    # Run the CSV Pipeline 
    pipeline = CSVPipeline(
        name= "Student Data Pipeline",
        required_columns= ["Name", "Score", "City"]
    )
    result = pipeline.run(
        input_path=sample_csv,
        output_path="data/processed/students_clean.csv"
    )
    
    print(f"\nPipeline object: {pipeline}")
    print(f"Row count: {len(pipeline)}")
    print(f"Drop rate: {result.drop_rate:.1%}")