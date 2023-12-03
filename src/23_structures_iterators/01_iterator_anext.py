# SuperFastPython.com
# example of one step of an asynchronous iterator
import asyncio

# define an asynchronous iterator
class AsyncIterator():
    # constructor, define some state
    def __init__(self):
        self.counter = 0

    # create an instance of the iterator
    def __aiter__(self):
        return self

    # return the next awaitable
    async def __anext__(self):
        # check for no further items
        if self.counter >= 10:
            raise StopAsyncIteration
        # increment the counter
        self.counter += 1
        # simulate work
        await asyncio.sleep(1)
        # return the counter value
        return self.counter

# main coroutine
async def main():
    # create the async iterator
    it = AsyncIterator()
    # step the iterator one iteration
    awaitable = anext(it)
    # get the result from one iteration
    result = await awaitable
    # report the result
    print(result)

# start the asyncio event loop
asyncio.run(main())
