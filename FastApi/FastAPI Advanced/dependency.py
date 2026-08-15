from fastapi import Header,HTTPException,APIRouter,Depends

router = APIRouter(prefix="/health",tags=["health"])

# pattern -1 : The simple value 

class Settings:
    def __init__(self):
        self.model_name = "iris classifier"
        
def get_settings():
    return Settings()

@router.get("")
def health_check(settings:Settings = Depends(get_settings)):
    return settings.model_name

# Pattern 2 - The Generator 
# def get_fake_db():
#     db = connect_to_db()
#     try: 
#         yield db
#     finally:
#         db.close()


#Pattern 3 - Dependency that reject the request 
def verify_api_key(x_api_key:str = Header(...))->str:
    if x_api_key!="dev_secret_key":
        raise HTTPException(status_code=401,detail="Unauthorized")
    return x_api_key

@router.predict("/predict")
def predicts(data,api_key:str = Depends(verify_api_key)):
    # runs only if verify_api_key didn't raise 
    return # just so it didn't go red 

