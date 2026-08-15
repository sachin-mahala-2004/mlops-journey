from fastapi import FastAPI
import logging
import time
logger = logging.getLogger("api")


app = FastAPI()
@app.middleware("http")
async def log_request(request,call_next):
    start_time = time.time()
    response = await call_next(request)
    duration_ms = (time.time() - start_time)*1000
    logger.info(f"{request.method} {request.url.path} - status={response.status_code} - {duration_ms:.2f}ms")
    return response

