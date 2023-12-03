# SuperFastPython.com
# example of checking if a task was canceled
import asyncio

# define a coroutine for a task
async def task_coroutine():
    # report a message
    print('executing the task')
    # block for a moment
    await asyncio.sleep(1)

# custom coroutine
async def main():
    # create and schedule the task
    task = asyncio.create_task(task_coroutine())
    # check if it is canceled
    print(f'>task canceled: {task.cancelled()}')
    # give the task a chance to run
    await asyncio.sleep(0.1)
    # cancel the task
    task.cancel()
    # wait for the task to be done
    await asyncio.sleep(0.1)
    # check if the task is canceled
    print(f'>task canceled: {task.cancelled()}')
    # check if the task is done
    print(f'>task done: {task.done()}')

# start the asyncio event loop
asyncio.run(main())
