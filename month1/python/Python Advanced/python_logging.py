import logging 
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s | %(levelname)s | %(message)s", 
    datefmt = "%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)

logger.debug("This won't show - level is INFO")
logger.info("Server Started")
logger.warning("Disk space runnning low")
logger.error("Failed to connect to database")
logger.critical("System is shuting down")


#----------------------------------------------------------------
print(f"\n {50*"="} \n")
# production setup: console + rotating file, different levels for each 
import logging
import os
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("mlops_app")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

os.makedirs("logs",exist_ok = True)
file_handler = RotatingFileHandler(
    "logs/app.log",
    maxBytes=5*1024*1024,
    backupCount=3
)

formatter = logging.Formatter("%(asctime)s | %(levelname)-8s | %(message)s ")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("Full details - only goes to the file")
logger.info("server started - goes to BOTH console and file")
logger.error("Something broke")

try:
    result = 10/0
except ZeroDivisionError:
    logger.exception("Division failed")
    
    
#-------------------------------------------------------------------
print(f"\n {50*"="} \n Exercise \n")
# Set up a logger that:
# - logs DEBUG and above to a rotating file "logs/test.log" (max 1MB, 2 backups)
# - logs WARNING and above to the console
# - includes timestamp, level, and message in the format

import logging 
from logging.handlers import RotatingFileHandler
import os
logger = logging.getLogger("mlops_app")
logger.setLevel(logging.DEBUG)

os.makedirs("logs",exist_ok=True)

file_handler = RotatingFileHandler(
    "logs/test.log",
    maxBytes= 1024*1024,
    backupCount=2
)
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

formatter = logging.Formatter("%(asctime)s | %(levelname)-8s | %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("This is a DEBUG message -> FILE ONLY")
logger.info("This is an INFO message -> FILE ONLY")
logger.warning("This is a WARNING message -> CONSOLE AND FILE")
logger.error("This is an ERROR message -> CONSOLE AND FILE")
logger.critical("This is a CRITICAL message -> CONSOLE AND FILE")