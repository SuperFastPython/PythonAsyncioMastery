# SuperFastPython.com
# example of a generator with async comprehension
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
    # loop over async generator with async comprehension
    results = [item async for item in async_generator()]
    # report results
    print(results)

# start the asyncio event loop
asyncio.run(main())
