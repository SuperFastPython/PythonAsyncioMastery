# SuperFastPython.com
# example of wait for with a condition
from random import random
import asyncio

# task coroutine
async def task(condition, work_list):
    # acquire the condition
    async with condition:
        # generate a random value between 0 and 1
        value = random()
        # block for a moment
        await asyncio.sleep(value)
        # add work to the list
        work_list.append(value)
        print(f'Task added {value}')
        # notify the waiting coroutine
        condition.notify()

# main coroutine
async def main():
    # create a condition
    condition = asyncio.Condition()
    # define work list
    work_list = list()
    # create and start many tasks
    _ = [asyncio.create_task(
        task(condition, work_list)) for _ in range(5)]
    # acquire the condition
    async with condition:
        # wait to be notified
        await condition.wait_for(
            lambda : len(work_list)==5)
        # report final message
        print(f'Done, got: {work_list}')

# start the asyncio event loop
asyncio.run(main())
