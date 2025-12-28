# Python asyncio

## 1. What Problem asyncio Solves

Python executes code synchronously by default. When a program waits for I/O (network, disk, timers), execution halts.

`asyncio` enables **concurrent I/O** using:

- A single thread
- An event loop
- Cooperative multitasking

asyncio is **not parallelism** and **not suitable for CPU-bound work**.

---

## 2. Async vs Concurrency vs Parallelism

- Sequential: tasks run one after another
- Concurrent: tasks interleave when waiting
- Parallel: tasks run simultaneously on multiple cores

asyncio is concurrent, single-threaded.

---

## 3. Coroutines

A coroutine is defined using `async def`.

```python
async def hello():
    return "hello"
```

Calling the function does not execute it.

```
coro = hello()  # coroutine object
```

## 4. Event Loop

The event loop:

* Schedules coroutines
* Suspends and resumes them
* Manages I/O readiness

Standard entry point:

```
import asyncio
asyncio.run(main())

```

Never call `asyncio.run()` inside another event loop.

```
await asyncio.sleep(1)
```

No `await` means blocking execution.

## 6. Sequential vs Concurrent Execution

Sequential (bad for I/O):

```
await task1()
await task2()
```

Concurrent:

```
await asyncio.gather(task1(), task2())
```

## 7. Tasks

A Task schedules a coroutine for execution.

```
task = asyncio.create_task(worker())
```

* Coroutines are lazy
* Tasks are scheduled immediately


## 8. gather vs create_task

* `asyncio.gather()` → structured concurrency, wait immediately
* `asyncio.create_task()` → background execution, await later


## 9. Blocking Code Pitfalls

Blocking calls freeze the event loop.

Bad:

```
time.sleep(1)

```

Good:

```
await asyncio.sleep(1)

```

Rule: if it blocks, it does not belong in async code.

## 10. Running Blocking Code Safely

```
await asyncio.to_thread(blocking_function)

```

Executes in a thread pool without blocking the loop.


## 11. Timeouts

```
await asyncio.wait_for(task(), timeout=3)

```

Raises `asyncio.TimeoutError`.
