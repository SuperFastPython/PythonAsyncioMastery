# SuperFastPython.com
# example of waiting for a coroutine that fails
from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = 1 * random()
    # report message
    print(f'>task got {value}')
    # block for a moment
    await asyncio.sleep(value)
    # fail with an exception
    raise Exception('Something bad happened')
    # report all done (never reached)
    print('>task done')

# main coroutine
async def main():
    # create a task
    task = task_coro(1)
    # execute and wait for the task without a timeout
    try:
        await asyncio.wait_for(task, timeout=2.0)
    except asyncio.TimeoutError:
        print('Gave up waiting, task canceled')
    except Exception as e:
        print(f'Task failed with: {e}')

# start the asyncio event loop
asyncio.run(main())
