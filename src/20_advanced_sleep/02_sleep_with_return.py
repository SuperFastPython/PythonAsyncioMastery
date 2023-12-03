# SuperFastPython.com
# example of the return value from sleep
import asyncio

# entry point coroutine
async def main():
    # get the sleep awaitable
    awaitable = asyncio.sleep(0.1)
    # report the awaitable
    print(type(awaitable))
    print(awaitable)
    # await the awaitable
    await awaitable

# start the asyncio event loop
asyncio.run(main())
