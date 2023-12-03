# SuperFastPython.com
# example of handling an exception when getting result
import asyncio

# define a coroutine for a task
async def task_coroutine():
    # report a message
    print('executing the task')
    # block for a moment
    await asyncio.sleep(1)
    # fail with an exception
    raise Exception('Something bad happened')
    # return a value (never reached)
    return 100

# custom coroutine
async def main():
    # report a message
    print('main coroutine started')
    # create and schedule the task
    task = asyncio.create_task(task_coroutine())
    # wait for the task to complete
    await asyncio.sleep(1.1)
    try:
        # get the result
        value = task.result()
    except Exception as e:
        print(f'Failed with: {e}')
    # report a final message
    print('main coroutine done')

# start the asyncio event loop
asyncio.run(main())
