# SuperFastPython.com
# example of getting an exception from a failed task
import asyncio

# define a coroutine for a task
async def task_coroutine():
    # report a message
    print('executing the task')
    # block for a moment
    await asyncio.sleep(1)
    # raise an exception
    raise Exception('Something bad happened')

# custom coroutine
async def main():
    # report a message
    print('main coroutine started')
    # create and schedule the task
    task = asyncio.create_task(task_coroutine())
    # wait for the task to complete
    await asyncio.sleep(1.1)
    # get the exception
    ex = task.exception()
    # report the details of the exception
    print(f'exception: {ex}')
    # report a final message
    print('main coroutine done')

# start the asyncio event loop
asyncio.run(main())
