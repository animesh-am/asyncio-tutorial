import asyncio

async def fetch_data(delay):
  print("Fetching data...")
  await asyncio.sleep(delay)
  print("Data fetched after", delay, "seconds")
  return {"data": "Sample data"}


async def main():
  print("Start of main coroutine")
  data = fetch_data(2)
  result = await data
  print("Received:", result)
  print("End of main coroutine")
  

asyncio.run(main())
  