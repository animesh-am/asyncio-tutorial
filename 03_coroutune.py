import asyncio


async def fetch_data(delay, id):
  print(f"Fetching data {id}...")
  await asyncio.sleep(delay)
  print(f"Data {id} fetched after", delay, "seconds")
  return {"data": f"Sample data {id}"}


async def main():
  task1 = asyncio.create_task(fetch_data(1, 2))
  task2 = asyncio.create_task(fetch_data(2, 3))
  task3 = asyncio.create_task(fetch_data(3, 1))
  
  result1 = await task1
  
  result2 = await task2
  
  result3 = await task3

  print(result1, result2, result3)  

asyncio.run(main())