import asyncio


async def fetch_data(delay, id):
  print(f"Fetching data {id}...")
  await asyncio.sleep(delay)
  print(f"Data {id} fetched after", delay, "seconds")
  return {"data": f"Sample data {id}"}


# taskgroup to manage multiple coroutines
async def main():
  tasks = []
  async with asyncio.TaskGroup() as tg:
    for i, sleep_time in enumerate([2,1,3], start=1):
      task = tg.create_task(fetch_data(i, sleep_time))
      tasks.append(task)
      
  results = [task.result() for task in tasks]

  for result in results:
    print(f"Received: {result}")
    

asyncio.run(main())