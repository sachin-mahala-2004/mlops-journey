# FastAPI Project 
This project is the complete version of previous "FastAPI_Fundamental_Project" , in this I used dependencies ,
specific routers , logging , middleware ,and CORS . 
Although there is still a lot of work remaining , like a real 
PostgreSQL Database connection and running a MachineLearning model for predictions instead of fake_predictions 

## Structure
```
main.py            - app creating, CORS, logging+latency middleware, router regestration
Dependencies.py    - get_settings, get_fake_db, verify_api_key
routers/           
items.py           - items CRUD(same as previous project but now organized APIRouter)
predict.py         - POST /predict (stub, no real model yet)
Health.py          - GET /health
```


## Setup 
```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

## Run 
```bash
uvicorn main:app --reload
```

## Try 
```bash
curl http://localhost:8000/health

curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -H "x-api-key: dev-secret-key" \
     -d '{"features":[1.0,2.0,3.0]}'
```

Then check `predictions.log` - The background task writes to it after the response is already sent.  