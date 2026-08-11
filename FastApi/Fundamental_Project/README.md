# Items API - FastAPI Fundamentals Project 
This Project consist of fundamentals of Fast API like all major decorators ,Path parameteres, Query Parameters, pydantic , status_codes etc. 

## Setup 
```bash 
python -m .venv venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

## Run 
```bash
uvicorn main:app --reload
```

Then open http://localhost:8000/docs for the intractive Swagger UI

## Endpoints 
 - GET     /               - health check 
 - GET     /items          - list all (optional ?q= and ?in_stock= filters)
 - GET     /items/{id}     - get one item
 - PUT     /items/{id}     - update an item
 - POST    /items          - create an item
 - DELETE  /items/{id}     - delete an item