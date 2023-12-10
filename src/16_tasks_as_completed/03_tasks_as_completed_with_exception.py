# SuperFastPython.com
# example of getting coroutine results with an exception
from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random()
    # block for a moment
    await asyncio.sleep(value)
    # check if the task should fail
    if value > 0.5:
        raise Exception('Something bad happened')
    # return the result
    return arg * value

# main coroutine
async def main():
    # create many coroutines
    coros = [task_coro(i) for i in range(10)]
    # get results as coroutines are completed
    for coro in asyncio.as_completed(coros):
        # get the result from the next to complete
        result = await coro # exception
        # report the result
        print(f'>got {result}')

# start the asyncio event loop
asyncio.run(main())
