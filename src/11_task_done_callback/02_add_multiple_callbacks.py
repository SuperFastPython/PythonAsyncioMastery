# SuperFastPython.com
# example of adding more than one done callback function
import asyncio

# custom done callback function
def callback1(task):
    # report a message
    print('Task is done')

# another custom done callback function
def callback2(task):
    # report a message
    print(f'Task: {task}')

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
    task.add_done_callback(callback1)
    # add another done callback function
    task.add_done_callback(callback2)
    # wait for the task to complete
    await task
    # report a final message
    print('main coroutine done')

# start the asyncio event loop
asyncio.run(main())
