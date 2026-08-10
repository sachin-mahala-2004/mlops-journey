# Normal function - computes EVERYTHING and returns all at once 
def get_squares(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result

squares = get_squares(1000000)

#Generator Function - computes one value at a time on demand
def get_squares_gen(n):
    for i in range(n):
        yield i**2
gen = get_squares_gen(10)       
print(list(gen))

#------------------------------------------------
# how yield works
def count_up_to(n):
    i = 1
    while i<=n:
        yield i
        i+=1

for num in count_up_to(5):
    print(num)

gen = count_up_to(3)
print(next(gen))  #1
print(next(gen))  # 2
print(next(gen))   # 3
# print(next(gen))   #error
        
# ----------------------------------------------------------------------------
print(f"{ 40*"="}")

# Real ML Ops use case 
# 1. Streaming 
def read_large_file(path):
    with open(path,"r") as f:
        for line in f:
            yield line.strip()

#Batching a stream (used constantly for model inference)
def batch_generator(data,batch_size):
    batch = []
    for item in data:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:               # yields the last partial batch 
        yield batch
        
print(f"\n {40*'='} \n Exercises: \n")

# Exercise 1: Write a generator function `even_numbers(n)` that yields even numbers up to n

def even_numbers(n):
    for num in range(n):
        if num%2 == 0 :
            yield num 

gen = even_numbers(15)
for num in gen:
    print(num)
    
# Exercise 2: Write a generator `read_in_chunks(path, chunk_size)` that yields chunk_size
#    LINES at a time from a file (not one line — a whole list of `chunk_size` lines)

def read_in_chunks(path, chunk_size):
    chunk = []
    with open(path,"r") as f:
        for line in f:
            chunk.append(line)
            if len(chunk) == chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk
        
 