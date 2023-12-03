# SuperFastPython.com
# example of waiting for a task with a timeout
import asyncio

# long running task
async def task(value):
    # sleep to simulate waiting
    await asyncio.sleep(10)
    # return value
    return value * 100

# asyncio entry point
async def main():
    # schedule the task
    running_task = asyncio.create_task(task(1))
    # allow the task to run
    await asyncio.sleep(0)
    # handle timeout
    try:
        # set a timeout
        async with asyncio.timeout(5):
            # wait for the task to complete
            result = await running_task
            # report the result
            print(result)
    except asyncio.TimeoutError:
        print(f'Timeout waiting')

# start the asyncio event loop
asyncio.run(main())
