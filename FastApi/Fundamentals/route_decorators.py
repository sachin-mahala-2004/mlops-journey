from fastapi import FastAPI
app = FastAPI()
app.get("/items")
def list_items():
    return {"items":[]}

app.post("/items")
def create_item():
    return {"message":"created"}

app.put("/items")
def update_items():
    return {"message":"updated"}

app.delete("/items")
def delete_item():
    return {"message":"deleted"}

import asyncio

app.get("/sync-example")
def sync_route():
    return {"ok":True}

app.get("/async-example")
async def async_route():
    result = await asyncio.sleep(2)
    return result 