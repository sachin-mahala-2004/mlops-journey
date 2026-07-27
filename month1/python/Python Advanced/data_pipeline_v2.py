import os
import asyncio
import logging
import time 
import csv
from contextlib import contextmanager
from logging.handlers import RotatingFileHandler
from typing import Iterator, Dict, Any, List 
from itertools import islice, chain

# --Logging setup - do this once at the top of your app -----------------------------
logger = logging.getLogger("data_pipeline")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

os.makedirs("logs", exist_ok=True)
file_handler = RotatingFileHandler("logs/pipeline.log" , maxBytes=2*1024*1024, backupCount=3)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s | %(levelname)-8s | %(message)s", datefmt="%H:%M:%S")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

#-- Context manager: times and logs each pipeline stage --------------------------------------------
@contextmanager
def pipeline_stage(stage_name: str):
    logger.info(f"Starting stage: {stage_name}")
    start = time.time()
    try:
        yield
    except Exception:
        logger.exception(f"Stage '{stage_name}' failed")
        raise 
    else: 
        elapsed = time.time() - start
        logger.info(f"Finished stage: {stage_name} ({elapsed:.2f}s)")
        

#-- Generator: reads rows one at a time - memory efficient for large files ---
def stream_csv_rows(path:str) -> Iterator[Dict[str,Any]]:
    with open(path,"r",newline="",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cleaned = {k: v.strip() for k,v in row.items()}
            if any(v for v in cleaned.values()):
                yield cleaned
    
def batch_rows(rows: Iterator[Dict[str,Any]],batch_size :int = 100) -> Iterator[List[Dict[str,Any]]]:
    batch = []
    for row in rows:
        batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch
        
#-- Async: simulated notifications afer pipeline finishes--------------------------------------
async def notify_pipeline_complete(pipeline_name:str,rows_processed:int) -> None:
    logger.info(f"Sending completion notification for {pipeline_name}...")
    await asyncio.sleep(1)   #simulates a real webhook/Slack/email call
    logger.info(f"Notified: {pipeline_name} processed {rows_processed} rows") 
    

# -- Full Pipeline run , using everything above ---------------------------------------------------
def run_pipeline(input_path:str) -> int:
    total_rows = 0 
    with pipeline_stage("load + clean (streamed)"):
        rows = stream_csv_rows(input_path)
        for batch in batch_rows(rows,batch_size = 2):
            total_rows += len(batch)
            logger.debug(f"Processed batch of {len(batch)} rows")
    
    with pipeline_stage("save summary"):
        with open("logs/summary.txt" ,"w") as f:
            f.write(f"Total rows processed: {total_rows}\n")
            
    return total_rows

if __name__ == "__main__" :
    os.makedirs("data",exist_ok=True)
    with open("data/sample.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "score"])
        for i in range(7):
            writer.writerow([f"student_{i}", i * 10])
        
    total = run_pipeline("data/sample.csv")
    asyncio.run(notify_pipeline_complete("Student Data Pipeline",total))

            
    