# SuperFastPython.com
# example of getting a result from a canceled task
import asyncio

# define a coroutine for a task
async def task_coroutine():
    # report a message
    print('executing the task')
    # block for a moment
    await asyncio.sleep(1)
    # return a value (never reached)
    return 99

# custom coroutine
async def main():
    # report a message
    print('main coroutine started')
    # create and schedule the task
    task = asyncio.create_task(task_coroutine())
    # wait for the task to complete
    await asyncio.sleep(0.1)
    # cancel the task
    task.cancel()
    # wait a moment for the task to be canceled
    await asyncio.sleep(0.1)
    # get the result
    value = task.result() # exception
    print(f'result: {value}')
    # report a final message
    print('main coroutine done')

# start the asyncio event loop
asyncio.run(main())
