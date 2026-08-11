from fastapi import FastAPI
app = FastAPI()
app.post("/items",status_code=201)
def create_item():
    return {"message":"created"}

app.delete("/items",status_code=204)
def remove_item():
    return {"message":"deleted"}

# Raising Errors (HTTP Exception )
items_db = {
    1: {"name": "Apple", "price": 1.50},
    2: {"name": "Banana", "price": 0.75}
}
from fastapi import HTTPException
app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404,detail="Item Not Found")
    return items_db[item_id]
    