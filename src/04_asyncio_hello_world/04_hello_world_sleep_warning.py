# SuperFastPython.com
# hello world program for asyncio that tries to sleep
import asyncio

# define a coroutine
async def main():
    # block
    asyncio.sleep(1) # warning
    # report a message
    print('Hello world')

# start the asyncio event loop
asyncio.run(main())
