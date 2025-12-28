import asyncio


async def fetch_data(delay, id):
  print(f"Fetching data {id}...")
  await asyncio.sleep(delay)
  print(f"Data {id} fetched after", delay, "seconds")
  return {"data": f"Sample data {id}"}


async def main():
  task1 = fetch_data(2, 1)
  task2 = fetch_data(2, 2)
  
  result1 = await task1
  print("Received:", result1)
  
  result2 = await task2
  print("Received:", result2)
  

asyncio.run(main())