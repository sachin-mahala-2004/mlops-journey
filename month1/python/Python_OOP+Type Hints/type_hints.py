# Basic type hints 

#Variables
name: str = "Arjun"
age: int = 20
score: float = 95.7
active: bool = True

#Function
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a+b

def safe_divide(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a/b

def log_message(message: str) -> None:
    print(f"[LOG] {message}")
    
# the typing module 
from typing import List, Dict, Tuple, Set, Optional, Union, Any, Callable

def process_names(names: List[str]) -> List[str]:
    return [name.upper() for name in names]

def get_scores() -> Dict[str,float]:
    return {"Alice": 85.0, "Bob": 92.5}

def get_range() -> Tuple[int,int]:
    return (0,100)

def find_item(items: List[str], target: str) -> Optional[int]:
    #Returns int(index) OR None if not found 
    try:
        return items.index(target)
    
    except ValueError:
         return None
     
def load_config(path:Optional[str]=None) ->Dict[str,Any]:
    return {}

def apply(func: Callable[[int],int],value: int) -> int :
    return func(value)