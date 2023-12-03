# SuperFastPython.com
# example of asyncio task group
import asyncio

# coroutine task
async def task1():
    # report a message
    print('Hello from coroutine 1')
    # sleep to simulate waiting
    await asyncio.sleep(1)

# coroutine task
async def task2():
    # report a message
    print('Hello from coroutine 2')
    # sleep to simulate waiting
    await asyncio.sleep(1)

# coroutine task
async def task3():
    # report a message
    print('Hello from coroutine 3')
    # sleep to simulate waiting
    await asyncio.sleep(1)

# asyncio entry point
async def main():
    # create task group
    async with asyncio.TaskGroup() as group:
        # run first task
        group.create_task(task1())
        # run second task
        group.create_task(task2())
        # run third task
        group.create_task(task3())
    # wait for all tasks to complete...
    print('Done')

# start the asyncio event loop
asyncio.run(main())
