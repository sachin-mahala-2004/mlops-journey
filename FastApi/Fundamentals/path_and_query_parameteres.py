from fastapi import FastAPI
app = FastAPI()

#path parameters

app.get("/items/{item_id}")
def get_item(item_id:int):
    return {"item":item_id}

# query parameters 
from typing import Optional
app.get("/items")
def list_items(q:Optional[str]=None ,limit: int=0):
    return {"item":q,"limit":limit}