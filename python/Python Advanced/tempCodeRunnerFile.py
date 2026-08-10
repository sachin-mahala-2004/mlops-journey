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