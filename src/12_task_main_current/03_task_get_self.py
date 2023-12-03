# SuperFastPython.com
# example of getting the task object from another task
import asyncio

# define another coroutine
async def another_coroutine():
    # report a message
    print('executing the task')
    # get the current task
    task = asyncio.current_task()
    # report its details
    print(task)

# define a main coroutine
async def main():
    # report a message
    print('main coroutine started')
    # create another task
    task = asyncio.create_task(another_coroutine())
    # await the task
    await task
    # report a final message
    print('main coroutine done')

# start the asyncio event loop
asyncio.run(main())