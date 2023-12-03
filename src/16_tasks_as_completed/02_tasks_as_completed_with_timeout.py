# SuperFastPython.com
# example of getting coroutine results with a timeout
from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random()
    # block for a moment
    await asyncio.sleep(value)
    # return the result
    return arg * value

# main coroutine
async def main():
    # create many coroutines
    coros = [task_coro(i) for i in range(10)]
    # handle a timeout
    try:
        # get results as coroutines are completed
        for coro in asyncio.as_completed(
            coros, timeout=0.5):
            # get the result from the next to complete
            result = await coro
            # report the result
            print(f'>got {result}')
    except asyncio.TimeoutError:
        print('Gave up after timeout')

# start the asyncio event loop
asyncio.run(main())
