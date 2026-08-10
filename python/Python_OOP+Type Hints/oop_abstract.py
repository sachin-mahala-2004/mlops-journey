from abc import ABC, abstractmethod
class BaseProcessor(ABC):
    
    def __init__(self,name:str):
        self.name = name 
    
    @abstractmethod    
    def load(self,path:str):
        """Load data form path. Must be implemented by subclass"""
        pass
    
    @abstractmethod
    def process(self,data):
        """Process data. Must be implemented by subclass"""
        pass
    
    @abstractmethod
    def save(self,data,path:str):
        """Save processed data. Must be implemented by subclass"""
        
    def run(self, input_path:str, output_path:str):
        """Template method - defines the pipeline flow"""
        print(f"[{self.name}] starting pipeline...")
        data = self.load(input_path)
        processed = self.process(data)
        self.save(processed,output_path)
        
class CSVProcessor(BaseProcessor):
    def load(self,path:str):
        import csv
        with open(path,"r") as f:
            return list(csv.DictReader(f))
        
    def process(self, data):
        return [row for row in data if row.get("active")==True]
    
    def save(self,data,path:str):
        import csv 
        with open(path,"w",newline="") as f:
            writer = csv.DictWriter(f,fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    
p = CSVProcessor("CSV Pipeline")

        