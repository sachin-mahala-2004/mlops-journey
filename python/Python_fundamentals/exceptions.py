# basic try/except 
try: 
   result =10/0
except ZeroDivisionError:
    print("Cannot divide by zero!")
    
try:
    data = {"key": "value"}
    print(data["missing"])     # KeyError
except KeyError as e:
    print(f"Key not found: {e}")
    
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        

    except TypeError:
        print(f"Error: Cannot divide {type(a)} by {type(b)}")
        
  
print(safe_divide(8,4))

try:
    result = 10 / 5

except ZeroDivisionError:
    print("Division by zero!")
else:
    print(f"Success! Result is {result}")
    
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero!")
else:
    print(result.upper())   # Still an error
    
try:
    result = 10 / 0
    print(result.upper())
except ZeroDivisionError:
    print("Division by zero!")
    
    
#custom exceptions
#define your own exception classes
class ModelNotLoadedError(Exception):
    pass

#raise ModelNotLoadedError("Something went wrong")

try:
    raise ModelNotLoadedError("something went wrong")
except ModelNotLoadedError as e:
    print(e)


#-------------------------------- 
#exercises 
# Exercise 1: Write safe_int(value) that returns int or None if conversion fails
# safe_int("42")     → 42
# safe_int("hello")  → None

def safe_int(number):
    try:
        return int(number)
    except ValueError: 
        print(f"Can't convert {number} to Interger")
        return None
    
print(safe_int("hello"))

# Exercise 3: Write safe_get(dictionary, key, default=None)
# Returns value if key exists, default if not — WITHOUT raising KeyError
def safe_get(dictionary,key,default=None):
    try:
        return dictionary[key]
    except KeyError as e:
        return default

# Exercise 4: Write validate_age(age) that raises ValueError if age < 0 or > 150     
def validate_age(age):
    if age>150 or age<0 :
        raise ValueError("Invalid age")
    
    
# Exercise 5: Write a function that reads a file and returns its content
# If file not found → return empty string
# If permission error → return None
# Finally → print "File operation complete"
def read_file(path):
    try: 
        with open(path,'rb') as f:
            return f.read()
    except FileNotFoundError :
        print("")
    except PermissionError:
        return None
    finally:
        print("File operation complete")
        
class InsufficientDataError(Exception):
    pass
def check_data(data):
    if len(data)<5:
        raise InsufficientDataError("List must contain atleast 5 elements")
 
try:
    check_data([1,2,3,4])
except InsufficientDataError as e:
    print(f" {e}")
   
 
 
# Exercise 7: Write a retry function
#def retry(func, max_attempts=3):
    # Try calling func() up to max_attempts times
    # If it keeps failing, raise the last exception
    #pass  
def retry(func,max_attempts=3):
    last_exception = None
    for _ in range(max_attempts):
        try:
            return func()
        except Exception as e:
            last_exception =e
    raise last_exception
       
def not_works():
    print("trying")
    raise ValueError("Something got wrong")

count = 0
def works():
    global count
    count+=1
    if count<3:
        raise ValueError("Error")
    return "Sucess!"

try:
   print(retry(not_works))
except Exception as e:
    print(e)
    
    
            
        
