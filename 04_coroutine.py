import asyncio


async def fetch_data(delay, id):
  print(f"Fetching data {id}...")
  await asyncio.sleep(delay)
  print(f"Data {id} fetched after", delay, "seconds")
  return {"data": f"Sample data {id}"}

# gather multiple coroutines and wait for all to complete
async def main():
  results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 1), fetch_data(3, 3))

  for result in results:
    print(f"Received: {result}")


asyncio.run(main())