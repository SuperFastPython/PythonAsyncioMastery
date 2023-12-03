# SuperFastPython.com
# example of checking the status of a failed task
import asyncio

# define a coroutine for a task
async def task_coroutine():
    # report a message
    print('executing the task')
    # block for a moment
    await asyncio.sleep(0.5)
    # raise an exception
    raise Exception('Something bad happened')

# custom coroutine
async def main():
    # create and schedule the task
    task = asyncio.create_task(task_coroutine())
    # check if it is done
    print(f'>task done: {task.done()}')
    # wait a moment
    await asyncio.sleep(0.1)
    # check if it is done
    print(f'>task done: {task.done()}')
    # wait for the task to complete
    await asyncio.sleep(0.5)
    # check if it is done
    print(f'>task done: {task.done()}')

# start the asyncio event loop
asyncio.run(main())
