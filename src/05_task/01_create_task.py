# SuperFastPython.com
# example of creating an asyncio task
import asyncio

# define a coroutine for a task
async def task_coroutine():
    # report a message
    print('Executing the task')
    # block for a moment
    await asyncio.sleep(1)

# custom coroutine
async def main():
    # report a message
    print('Main coroutine started')
    # create and schedule the task
    task = asyncio.create_task(task_coroutine())
    # wait for the task to complete
    await task
    # report a final message
    print('Main coroutine done')

# start the asyncio event loop
asyncio.run(main())
