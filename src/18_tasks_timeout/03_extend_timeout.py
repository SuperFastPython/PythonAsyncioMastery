# SuperFastPython.com
# example of extending a timeout delay
import asyncio

# long running task
async def task(value):
    # sleep to simulate waiting
    await asyncio.sleep(10)
    # return value
    return value * 100

# asyncio entry point
async def main():
    # handle timeout
    try:
        # set a timeout
        async with asyncio.timeout(5) as timeout:
            # wait a moment
            await asyncio.sleep(4)
            # set a deadline 5 seconds in the future
            loop = asyncio.get_running_loop()
            deadline = loop.time() + 11
            # set the new deadline
            timeout.reschedule(deadline)
            # execute long running task
            result = await task(1)
            # report the result
            print(result)
    except asyncio.TimeoutError:
        print(f'Timeout waiting')

# start the asyncio event loop
asyncio.run(main())
