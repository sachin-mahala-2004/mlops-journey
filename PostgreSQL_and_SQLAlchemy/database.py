from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from dotenv import load_dotenv
import os
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(
    DATABASE_URL,
    pool_size = 5, 
    max_overflow = 10,
    pool_timeout= 30,
    pool_pre_ping = True,
    pool_recycle = 1800)

SessionLocal = sessionmaker(
    engine = engine,
    autoflush = False,
    expire_on_commit=False)

class Base(DeclarativeBase):
    pass
