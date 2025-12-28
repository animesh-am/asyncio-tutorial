import asyncio


async def main():
  print("Start of main coroutine")


# main() -> Coroutine object that runs the main coroutine

asyncio.run(main())