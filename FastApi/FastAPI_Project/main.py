import logging
import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routers import Health,items,predict

# -- Logging setup (same pattern as Days 14-15)

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level = logging.INFO,
    datefmt="%H:%M:%S",
)

logger = logging.getLogger("api")

app = FastAPI(title="Items + Predict API",version = "0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_headers=["*"],
    allow_methods=["*"],
)

#-- Custom middleware: logs every request + how long it took -------
@app.middleware("http")
async def log_requests(request:Request,call_next):
    start_time = time.time()
    response = await call_next(request)
    duration_ms = (time.time() - start_time)*1000
    logger.info(
        f"{request.method} {request.url.path}"
        f"- status={response.status_code} - {duration_ms:.2f}ms"
    )
    return response

# --Register routers -each domain's routes stay in their own file 
app.include_router(items.router)
app.include_router(Health.router)
app.include_router(predict.router)

@app.get("/")
def root():
    return {"message":"API is running - see/docs"}
