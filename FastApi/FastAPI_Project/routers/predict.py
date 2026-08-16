from fastapi import APIRouter,Depends,BackgroundTasks
from pydantic import BaseModel
from Dependencies import Settings,get_settings,verify_api_key
router = APIRouter(prefix="/predict",tags=["predict"])

class PredictRequest(BaseModel):
    features:list[float]
    
class PredictResponse(BaseModel):
    predictions:float
    model_version:str

def log_prediction(features:list[float],predictions:float)->None:
    with open("predicitions.log","a") as f:
        f.write(f"features={features} -> predictions={predictions}\n")
        
@router.post("",response_model=PredictResponse)
def Predict(
    data:PredictRequest,
    background_tasks:BackgroundTasks,
    settings: Settings = Depends(get_settings),
    api_key:str=Depends(verify_api_key),
):
    fake_predictions = sum(data.features)/len(data.features) if data.features else 0.0
    background_tasks.add_task(log_prediction,data.features,fake_predictions)
    return PredictResponse(predictions=fake_predictions,model_version=settings.model_name)
