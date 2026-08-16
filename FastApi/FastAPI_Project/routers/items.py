from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from typing import Optional
router = APIRouter(prefix="/items",tags=["items"])

class ItmeRequest(BaseModel):
    name:str
    price:float
    in_stock:bool=True
    
class ItemResponse(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool
    
next_id = 1
items_db : dict[int,dict]={}

@router.get("",response_model=list[ItemResponse])
def list_items(q:Optional[str]=None,in_stock:Optional[bool]=None):
    result = list(items_db.values())
    if q:
        result = [i for i in result if q.lower() in i["name"].lower()]
        
    if in_stock is not None:
        result = [i for i in result if i["in_stock"]==in_stock]
    return result

@router.get("/{item_id}",response_model=ItemResponse)
def get_item(item_id:int):
    if item_id not in items_db:
        raise HTTPException(status_code=404 , detail="Item not Found")
    return items_db[item_id]

@router.post("",response_model=ItemResponse,status_code=201)
def create_item(item:ItmeRequest):
    global next_id
    next_item = {"id":next_id,**item.model_dump()}
    items_db[next_id] = next_item
    next_id+=1
    return next_item

@router.put("/{item_id}",response_model=ItemResponse,status_code=201)
def update_item(item_id:int,item:ItmeRequest):
    if item_id not in items_db:
        raise HTTPException(status_code=404 , detail="Item not Found")
    updated_item = {"id":item_id,**item.model_dump()}
    items_db[item_id] = updated_item
    return updated_item

@router.delete("{item_id}",status_code=204)
def delete_item(item_id:int)-> None:
    if item_id not in items_db:
        raise HTTPException(status_code=404,detail="Item not found")
    del items_db[item_id]
    return None