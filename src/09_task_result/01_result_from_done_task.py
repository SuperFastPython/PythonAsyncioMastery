# SuperFastPython.com
# example of getting a result from a done task
import asyncio

# define a coroutine for a task
async def task_coroutine():
    # report a message
    print('executing the task')
    # block for a moment
    await asyncio.sleep(1)
    # return a value
    return 99

# custom coroutine
async def main():
    # report a message
    print('main coroutine started')
    # create and schedule the task
    task = asyncio.create_task(task_coroutine())
    # wait for the task to complete
    await task
    # get the result
    value = task.result()
    # report the task result
    print(f'result: {value}')
    # report a final message
    print('main coroutine done')

# start the asyncio event loop
asyncio.run(main())
