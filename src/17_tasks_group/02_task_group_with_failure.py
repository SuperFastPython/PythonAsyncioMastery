# SuperFastPython.com
# example of asyncio task group with a failed task
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
    await asyncio.sleep(0.5)
    # fail with an exception
    raise Exception('Something bad happened')

# coroutine task
async def task3():
    # report a message
    print('Hello from coroutine 2')
    # sleep to simulate waiting
    await asyncio.sleep(1)

# asyncio entry point
async def main():
    # handle exceptions
    try:
        # create task group
        async with asyncio.TaskGroup() as group:
            # run first task
            t1 = group.create_task(task1())
            # run second task
            t2 = group.create_task(task2())
            # run third task
            t3 = group.create_task(task3())
    except:
        pass
    # check the status of each task
    print(f't1: done={t1.done()}, can={t1.cancelled()}')
    print(f't2: done={t2.done()}, can={t2.cancelled()}')
    print(f't3: done={t3.done()}, can={t3.cancelled()}')

# start the asyncio event loop
asyncio.run(main())
