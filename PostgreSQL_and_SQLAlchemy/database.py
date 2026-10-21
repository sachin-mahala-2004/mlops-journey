import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker,DeclarativeBase , Session


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,pool_size=5, max_overflow=10, pool_pre_ping=True, pool_timeout=30, pool_recycle=1800, echo=False
)               

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

# The FastAPI dependency 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# A plain context manager for scripts and background jobs , where there is no FastAPI to resolve the dependency for you 
class session_scope:
    def __enter__(self)->Session:
        self.db = SessionLocal()
        return self.db
    
    def __exit__(self,exc_type,exc_value,traceback):
        try:
            if exc_type is None:
                self.db.commit()
            else: 
                self.db.rollback()
        finally:
            self.db.close()
        return False

def check_connection() -> str:
    """ Prove that the database is reachable. Returns the server version."""
    with engine.connect() as conn:
        conn.execute(text("SELECT verison()")).scalar_one()
        