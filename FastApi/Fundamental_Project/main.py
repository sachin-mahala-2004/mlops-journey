from fastapi import FastAPI, HTTPException
from typing import Optional,Dict,List
from pydantic import BaseModel

app = FastAPI()
#--In memory "Database" - a real DB (PostgreSQL) comes in days 70-75
# Just a dict for now : {id: item_dict}
items_db :Dict[int,Dict] = {}
# it looks like this after 2 items 
#items_db = {
#     1: {"id": 1, "name": "phone", "price": 230.0, "in_stock": True},
#     2: {"id": 2, "name": "tv", "price": 250.0, "in_stock": False}  # Updated!
# }

next_id = 1

# -- Pydantic schemas - separate INPUT (what client sends) from 
#    OUTPUT (what server returns). This is standard practice , not overkill. --
class ItemCreate(BaseModel):
    name: str
    price: float
    in_stock: bool = True
    
class ItemResponse(BaseModel):
    id: int 
    name: str
    price: float
    in_stock:bool = True
    
# -- Routes ---------------------------------
@app.get("/")
def root():
    return {"message":"Items API is running"}

@app.get("/items",response_model=list[ItemResponse])
def list_items(q:Optional[str]=None, in_stock: Optional[bool]=None):
    results = list(items_db.values())
    if q:
        results = [i for i in results if q.lower() in i["name"].lower()]
    if in_stock is not None:
        results = [i for i in results if i["in_stock"]==in_stock]
    return results
    
@app.get("/items/{item_id}",response_model=ItemResponse)
def get_item(item_id:int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not Found")
    return items_db[item_id]

@app.post("/items",response_model=ItemResponse,status_code=202)
def create_item(item:ItemCreate):
    global next_id
    new_item = {"id":next_id,**item.model_dump()}
    items_db[next_id]=new_item
    next_id+=1
    return new_item

@app.put("/items/{item_id}",response_model=ItemResponse)
def update_item(item_id:int,item:ItemCreate):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not Found")
    updated_item = {"id":item_id,**item.model_dump()}
    items_db[item_id] = updated_item
    return updated_item

@app.delete("/items/{item_id}",status_code=204)
def delete_item(item_id:int):
    if item_id not in items_db:
            raise HTTPException(status_code=404, detail="Item not Found")
    del items_db[item_id]
    return None