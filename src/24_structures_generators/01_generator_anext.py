# SuperFastPython.com
# example of one step of an asynchronous generator
import asyncio

# define an asynchronous generator
async def async_generator():
    # normal loop
    for i in range(10):
        # block to simulate doing work
        await asyncio.sleep(1)
        # yield the result
        yield i

# main coroutine
async def main():
    # create the async generator
    gen = async_generator()
    # step the generator one iteration
    awaitable = anext(gen)
    # get the result from one iteration
    result = await awaitable
    # report the result
    print(result)

# start the asyncio event loop
asyncio.run(main())
