# SuperFastPython.com
# example of an asyncio barrier with a timeout and abort
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
    try:
        # wait on all other tasks to complete
        await barrier.wait()
    except asyncio.BrokenBarrierError:
        # report the task is no longer waiting
        print(f'Task {number} aborted waiting...')

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
    try:
        # wait for tasks to complete with a timeout
        async with asyncio.timeout(5):
            # wait on the barrier
            await barrier.wait()
            # report once all tasks are done
            print('All tasks have their result')
    except asyncio.TimeoutError:
        # abort the barrier
        print('Main is aborting the barrier')
        await barrier.abort()
    # wait around
    await asyncio.sleep(5)

# start the asyncio event loop
asyncio.run(main())
