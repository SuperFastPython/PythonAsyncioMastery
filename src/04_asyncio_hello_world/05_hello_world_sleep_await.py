# SuperFastPython.com
# hello world program for asyncio that sleeps
import asyncio

# define a coroutine
async def custom_coroutine():
    # block
    await asyncio.sleep(1)
    # report a message
    print('Hello world')

# start the asyncio event loop
asyncio.run(custom_coroutine())
