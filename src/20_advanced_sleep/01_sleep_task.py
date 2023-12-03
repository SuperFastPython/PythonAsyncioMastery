# SuperFastPython.com
# example of sleeping a task
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
    # execute another task
    await asyncio.create_task(custom_coro())

# start the asyncio event loop
asyncio.run(main())
