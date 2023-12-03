# SuperFastPython.com
# example of getting the task from another coroutine
import asyncio

# define another coroutine
async def another_coroutine():
    # report a message
    print('executing the coroutine')
    # get the current task
    task = asyncio.current_task()
    # report its details
    print(task)

# define a main coroutine
async def main():
    # report a message
    print('main coroutine started')
    # wait another coroutine
    await another_coroutine()
    # report a final message
    print('main coroutine done')

# start the asyncio event loop
asyncio.run(main())
