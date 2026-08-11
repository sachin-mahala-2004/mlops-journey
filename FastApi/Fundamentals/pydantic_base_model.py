from pydantic import BaseModel
from fastapi import FastAPI

class ItemCreate(BaseModel):
    name: int 
    price: float
    in_stock: bool = True
    
class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool
  
app = FastAPI()

app.post("items/",response_model=ItemResponse)
def create_item(item: ItemCreate):
    # 'item' arrives here ALREADY validated — if the client sent
    # price as text or forgot 'name' entirely, FastAPI already
    # rejected the request with a 422 before this function even ran.
    return 
