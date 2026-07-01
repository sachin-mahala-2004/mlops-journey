# *args and **kwargs
# *args - variable number of positional arguments 

def add(*args):         #Take all extra positional arguments and pack them into a tuple
    return sum(args)

print(add(2,3,4,5,5))

# args is a TUPLE inside the function
def show_args(*args):
    print(type(args))   # <class 'tuple'>
    for i, arg in enumerate(args):
        print(f"  arg[{i}] = {arg}")

show_args("hello", 42, [1, 2, 3])

#---------------
# **kwargs - variable number of keyword arguments 

def show_kwargs(**kwargs):     #**kwargs, Python packs these keyword arguments into a dictionary
    print(type(kwargs))
    for key,value in kwargs.items():
        print(f"{key} = {value}")

show_kwargs(name='Arjun',age=20,city='Jaipur')
        
        
def person(name, age):
    print(name, age)

data = {"name": "Alice", "age": 25}

person(**data) 
#python converts to : person(name = 'Alice',age = 25)


#Real use case: build config dict 
def create_model_config(**kwargs):
    default = {"learning_rate": 0.01, "epochs": 10, "batch_size": 32}
    default.update(kwargs)  #override defaults with provided values 
    return default

config = create_model_config(epoch = 50, dropout=0.2)
print(config)


#Combining all argument types 
#Order MUST be : regular args -> *args -> keyword-only -> **kwargs
def process(required,*args,separator='---',**kwargs):
    print(f"Required: {required}")
    print(f"Extra positional: {args}")
    print(f"Separator: {separator}")
    print(f"Keyword args: {kwargs}")
    
process("hello",1,2,3, separator="===", name="Arjun", debug=True)

## Unpacking with *and **when calling functions
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))      # 6 — unpack list as positional args

params  = {"a": 1, "b": 2, "c": 3}
print(add(**params))      # 6 — unpack dict as keyword args


# Merge two dicts(very common in MLOps for configs)
defaults = {"lr": 0.01, "epochs": 10}
custom   = {"epochs": 50, "dropout": 0.2}
merged = {**defaults,**custom}
print(merged)


#------------------------------------------------
#Exercise 1: Write a function multiply(*args) that multiplies all arguments
def multiply(*args):
    prod = 1
    for arg in args:
        prod=arg*prod
    return prod

print(multiply(1,2,3,4,5))

# Exercise 2: Write a function that prints all kwargs formatted nicely
# show_config(host="localhost", port=8000, debug=True)
# host    : localhost
# port    : 8000
# debug   : True

def show_config(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")
        
show_config(host="localhost", port=8000, debug=True)

# Exercise 3: Write a function greet(name, *titles) that combines titles
# greet("Arjun", "Dr", "Prof") → "Hello, Dr Prof Arjun!"
def greet(name , *titles):
    print(f"Hello, {' '.join(title for title in titles)} {name}!")

greet("Arjun", "Dr", "Prof")

#Exercise 6:
def get_max_min(a, b, c, d):
    return max(a,b,c,d), min(a,b,c,d)

values = [4, 7, 2, 9]
print(get_max_min(*values))

# Exercise 8: Write a logging function log(level, *messages, **context)
# log("INFO", "Server started", "Port bound", host="localhost", port=8000)
# [INFO] Server started | Port bound | host=localhost port=8000
def logging(level,*messages,**context):
    print(f"[{level}] {" | ".join(messages)} | {' '.join(f"{key}={value}" for key,value in context.items())}")

logging("INFO", "Server started", "Port bound", host="localhost", port=8000)        

