# SuperFastPython.com
# example of an asyncio barrier
from random import random
import asyncio

# coroutine that prepares work and waits on a barrier
async def work(barrier, number):
    # generate a unique value
    value = random() * 10
    # suspend for a moment to simulate work
    await asyncio.sleep(value)
    # report result
    print(f'Task {number} done, {value}, waiting...')
    # wait on all other tasks to complete
    await barrier.wait()

# main coroutine
async def main():
    # create a barrier
    n_tasks = 5
    barrier = asyncio.Barrier(n_tasks + 1)
    # issue all of the tasks
    _ = [asyncio.create_task(
        work(barrier, i)) for i in range(n_tasks)]
    # wait for all tasks to finish
    print('Main is waiting on all results...')
    async with barrier:
        # report once all tasks are done
        print('All tasks have their result')

# start the asyncio event loop
asyncio.run(main())
