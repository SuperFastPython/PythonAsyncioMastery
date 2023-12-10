# SuperFastPython.com
# example of starting many tasks and awaiting them
import asyncio

# coroutine for a task
async def task_coroutine(value):
    # report a message
    print(f'task {value} is running')
    # block for a moment
    await asyncio.sleep(1)

# define a main coroutine
async def main():
    # report a message
    print('main coroutine started')
    # start many tasks
    for i in range(10):
        asyncio.create_task(task_coroutine(i))
    # allow some of the tasks time to start
    await asyncio.sleep(0.1)
    # get all tasks
    tasks = asyncio.all_tasks()
    # wait for all tasks to complete
    for task in tasks:
        await task # exception

# start the asyncio event loop
asyncio.run(main())
