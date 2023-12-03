# SuperFastPython.com
# example of waiting for a task that is canceled
from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = 1 + random()
    # report message
    print(f'>task got {value}')
    # block for a moment
    await asyncio.sleep(value)
    # report all done
    print('>task done')

# another coroutine that cancels a task
async def task_cancel(other_task):
    # wait a moment
    await asyncio.sleep(0.3)
    # cancel the other task
    other_task.cancel()

# main coroutine
async def main():
    # create a task
    task = asyncio.create_task(task_coro(1))
    # create the wait for coroutine
    wait_coro = asyncio.wait_for(task, timeout=1)
    # create and run the cancel task
    asyncio.create_task(task_cancel(task))
    # await the wait-for coroutine
    try:
        await wait_coro
    except asyncio.TimeoutError:
        print('Gave up waiting, task canceled')
    except asyncio.CancelledError:
        print('Task was canceled externally')
        print(task)

# start the asyncio event loop
asyncio.run(main())
