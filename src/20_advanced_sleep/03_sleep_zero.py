# SuperFastPython.com
# example of sleeping for zero seconds
import asyncio

# custom coroutine
async def custom_coro():
    # report a message
    print('task running')
    # block for a moment
    await asyncio.sleep(1)
    # report a message
    print('task done')

# entry point coroutine
async def main():
    # execute another coroutine
    task = asyncio.create_task(custom_coro())
    print('main is blocking now')
    # sleep while the task is running
    await asyncio.sleep(0)
    # report a message
    print('main is done blocking')
    # wait for the task to complete
    await task

# start the asyncio event loop
asyncio.run(main())
