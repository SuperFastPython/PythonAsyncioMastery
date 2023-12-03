# SuperFastPython.com
# example of checking if an asyncio task is done
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
    # check if it is done
    print(f'>task done: {task.done()}')
    # wait a moment
    await asyncio.sleep(0.1)
    # check if it is done
    print(f'>task done: {task.done()}')
    # wait for the task to complete
    await task
    # check if it is done
    print(f'>task done: {task.done()}')

# start the asyncio event loop
asyncio.run(main())
