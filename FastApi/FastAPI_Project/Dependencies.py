""" 
Shared depencdencies - functions used with Depends() across multiple routers. 
This is the single biggest reason Dependency Injection matters: write validataion or 
setup logic ONCE here, reuse it on any route that needs it.
"""
from fastapi import Header,HTTPException


class Settings:
    def __init__(self):
        self.model_name = "iris_classifier"
        self.api_version = "0.1.0"
        
def get_settings() -> Settings:
    return Settings()

def get_fake_db():
    db = {"connection":"fake-db-session-object"}
    print("[dependency] opening fake db connection")
    try: 
        yield db
    finally:
        print("[dependency] closing fake db connection")
        
def verify_api_key(x_api_key: str = Header(...))->str:
    if x_api_key!="dev-secret-key":
        raise HTTPException(status_code=401,detail="Invalid or missing API key")
    return x_api_key
    