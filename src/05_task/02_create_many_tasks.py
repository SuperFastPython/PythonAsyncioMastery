# SuperFastPython.com
# example of creating many asyncio tasks
import asyncio

# define a coroutine for a task
async def task_coroutine(number):
    # report a message
    print(f'>Executing the task {number}')
    # block for a moment
    await asyncio.sleep(1)

# custom coroutine
async def main():
    # report a message
    print('Main coroutine started')
    # create and schedule many tasks
    tasks = [asyncio.create_task(
        task_coroutine(i)) for i in range(20)]
    # wait for each task to complete
    for task in tasks:
        await task
    # report a final message
    print('Main coroutine done')

# start the asyncio event loop
asyncio.run(main())
