class Timer:
    def __enter__(self):
       import time
       self.start = time.time()
       return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        import time
        elapsed = time.time() - self.start 
        print(f"Took {elapsed:.4f}s")
        return False
    
with Timer():
    total = sum(x**2 for x in range(1000000))

    
#-----------------------------------------------------------------
print(f"\n {40*'='} \n" )
# What __exit__'s three arguments are for 
class SafeOperation:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"Caught an error({exc_type}): {exc_value}")
            return True
        return False
    
with SafeOperation():
    result = 10/0
print("Program continues")

#---------------------------------------------------
print(f"\n {40*'='} \n" )
# Real MLOps example - a DB connection manager

class DatabaseConnection:
    def __init__(self,db_url):
        self.db_url = db_url
        
    def __enter__(self):
        print(f"Connecting to {self.db_url}")
        self.conn = f"<connection: {self.db_url}>"
        return self.conn
    
    def __exit__(self,exc_type,exc_value,traceback):
        print("Closing connection")
        self.conn = None
        return False 
    
with DatabaseConnection("postgresql://localhost/mlops") as conn:
    print(conn)
    print(type(conn))     
    
    
#--------------------------------------------------------------------------
print(f"\n {40*'='} \n Exercise \n" )
#  Write a class-based context manager `SuppressErrors` that:
# - prints "Starting..." on enter
# - if any exception happens inside, prints the error and SUPPRESSES it
# - if no exception, prints "Done, no errors"

class SuppressErrors:
    def __enter__(self):
        print("Starting")
    def __exit__(self, exc_type, exc, tb):
        if exc_type is not None:
            print(f"Error Type ({exc_type}:{exc})")
            return True
        if exc_type is None:
            print("Done")
        return False
print("--- Test 1: With an Error ---")
with SuppressErrors():
    result = 10 / 0    # This would normally crash the whole script

print("\n--- Test 2: Without an Error ---")
with SuppressErrors():
    result = 10 / 2    

print("\nProgram finished successfully!")

#--------------------------------------------------------------------------------------
# Context Managers the Easy Way: @contextmanager
from contextlib import contextmanager
import time 
@contextmanager
def timer(name):
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start 
        print(f"[{name}] took {elapsed}s")
        
with timer("Data Loading") :
    data = [i for i in range(1000000)]
    
@contextmanager
def open_file(path,mode):
    f = open(path,mode)
    try:
        yield f
    finally:
        f.close()
    
with open_file("test.txt","w") as f:
    f.write('hello')
    
with open_file("test.txt","r") as input_file, open_file("output.txt","w") as output_file:
    output_file.write(input_file.read())

#---------------------------------------------------------------------


    