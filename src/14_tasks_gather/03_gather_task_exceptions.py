# SuperFastPython.com
# example of gather with returned exceptions
import asyncio

# coroutine used for a task
async def task_coro(value):
    # report a message
    print(f'>task {value} executing')
    # sleep for a moment
    await asyncio.sleep(1)
    # check for failure
    if value == 0:
        raise Exception('Something bad happened')
    # return a value
    return value * 10

# coroutine used for the entry point
async def main():
    # report a message
    print('main starting')
    # create many coroutines
    tasks = [asyncio.create_task(
        task_coro(i)) for i in range(10)]
    # run the tasks
    results = await asyncio.gather(*tasks,
        return_exceptions=True)
    # report results
    print(results)
    # report a message
    print('main done')

# start the asyncio event loop
asyncio.run(main())
