from fastapi import BackgroundTasks,APIRouter
router = APIRouter(prefix="/predict",tags=["predict"])

def logging(features:list,prediction:float):
    with open("logging.txt","a") as f:
        f.write(f"{features} -> {prediction}\n")
 
def run_model(data):
    return 3*data+4  
     
@router.post("")
def predict(data,background_task:BackgroundTasks):
    result = run_model(data)
    background_task.add_task(logging,data,result)
    return result    # client gets this immeditaly , logging happens after that 
    
