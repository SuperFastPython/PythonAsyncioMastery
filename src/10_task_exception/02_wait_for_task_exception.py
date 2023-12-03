# SuperFastPython.com
# example of handling a task exception when await
import asyncio

# define a coroutine for a task
async def task_coroutine():
    # report a message
    print('executing the task')
    # block for a moment
    await asyncio.sleep(1)
    # fail with an exception
    raise Exception('Something bad happened')

# custom coroutine
async def main():
    # report a message
    print('main coroutine started')
    # create and schedule the task
    task = asyncio.create_task(task_coroutine())
    try:
        # wait for the task to complete
        await task
    except Exception as e:
        # report the exception
        print(f'Failed with: {e}')
    # report a final message
    print('main coroutine done')

# start the asyncio event loop
asyncio.run(main())
