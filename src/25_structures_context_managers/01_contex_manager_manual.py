# SuperFastPython.com
# example of using an async context manager manually
import asyncio

# define an asynchronous context manager
class AsyncContextManager:
    # enter the async context manager
    async def __aenter__(self):
        # report a message
        print('>entering the context manager')
        # block for a moment
        await asyncio.sleep(0.5)

    # exit the async context manager
    async def __aexit__(self, exc_type, exc, tb):
        # report a message
        print('>exiting the context manager')
        # block for a moment
        await asyncio.sleep(0.5)

# define a simple coroutine
async def custom_coroutine():
    # create and use the asynchronous context manager
    manager = AsyncContextManager()
    # get the awaitable for entering the manager
    enter_awaitable = manager.__aenter__()
    # await the entry
    await enter_awaitable
    # execute the body
    print(f'within the manager')
    # get the awaitable for exiting the manager
    exit_awaitable = manager.__aexit__(None, None, None)
    # await the exit
    await exit_awaitable

# start the asyncio event loop
asyncio.run(custom_coroutine())
