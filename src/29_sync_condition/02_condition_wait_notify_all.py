# SuperFastPython.com
# example of wait/notify all with an asyncio condition
from random import random
import asyncio

# task coroutine
async def task(condition, number):
    # report a message
    print(f'Task {number} waiting...')
    # acquire the condition
    async with condition:
        # wait to be notified
        await condition.wait()
    # generate a random number between 0 and 1
    value = random()
    # block for a moment
    await asyncio.sleep(value)
    # report a result
    print(f'Task {number} got {value}')

# main coroutine
async def main():
    # create a condition
    condition = asyncio.Condition()
    # create and start many tasks
    tasks = [asyncio.create_task(
        task(condition, i)) for i in range(5)]
    # allow the tasks to run
    await asyncio.sleep(1)
    # acquire the condition
    async with condition:
        # notify all waiting tasks
        condition.notify_all()
    # wait for all tasks to complete
    _ = await asyncio.wait(tasks)

# start the asyncio event loop
asyncio.run(main())
