import asyncio

async def say_hello():
    print("hello")
    await asyncio.sleep(2) #simulates waiting on something (eg. an API call)
    print("world")
asyncio.run(say_hello())

#-----------------------------------------------------------
# Running things conncurently 

async def fetch_data(name,delay):
    print(f"Start Fetching {name}")
    await asyncio.sleep(delay)
    print(f"Done fetching {name}")
    return f"{name} result"

async def main():
    results = await asyncio.gather(
        fetch_data("A",3),
        fetch_data("B",2),
        fetch_data("C",1),
    ) 
    print(results)
    
asyncio.run(main())
    
#--------------------------------------------------------------------------------------  
print(f"\n {50*"="} \n")
# Write 3 async functions simulating: fetch_user(1s), fetch_orders(2s), fetch_reviews(1.5s)
# Run all 3 concurrently with asyncio.gather and print how long the total took
# (Hint: it should take ~2 seconds, not 4.5)
import asyncio
async def fetch_user(delay):
    print(f"Fetching User")
    await asyncio.sleep(delay)
    print("User Fetched") 
    
async def fetch_orders(delay):
    print(f"Fetching Orders")
    await asyncio.sleep(delay)
    print("Orders Fetched") 
    
async def fetch_reviews(delay):
    print(f"Fetching Reviews")
    await asyncio.sleep(delay)
    print("Reviews Fetched") 
    
async def main():
    import time
    start = time.time()
    await asyncio.gather(
        fetch_user(1),
        fetch_orders(2),
        fetch_reviews(1.5)
    )
    elapsed = time.time() - start
    print(f"Total time took : {elapsed:.2f}s")

asyncio.run(main())
 
    
