# SuperFastPython.com
# example of adding a done callback function to a task
import asyncio

# custom done callback function
def callback(task):
    # report a message
    print('Task is done')

# define a coroutine for a task
async def task_coroutine():
    # report a message
    print('executing the task')
    # block for a moment
    await asyncio.sleep(1)

# custom coroutine
async def main():
    # report a message
    print('main coroutine started')
    # create and schedule the task
    task = asyncio.create_task(task_coroutine())
    # add a done callback function
    task.add_done_callback(callback)
    # wait for the task to complete
    await task
    # report a final message
    print('main coroutine done')

# start the asyncio event loop
asyncio.run(main())
