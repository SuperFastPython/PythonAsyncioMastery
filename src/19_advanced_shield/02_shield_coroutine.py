# SuperFastPython.com
# example of shielding a coroutine from cancellation
import asyncio

# define a simple asynchronous
async def simple_task(number):
    # block for a moment
    await asyncio.sleep(1)
    # return the argument
    return number

# cancel the given task after a moment
async def cancel_task(task):
    # block for a moment
    await asyncio.sleep(0.2)
    # cancel the task
    was_cancelled = task.cancel()
    print(f'cancelled: {was_cancelled}')

# define a simple coroutine
async def main():
    # create the coroutine
    coro = simple_task(1)
    # created the shielded task
    shielded = asyncio.shield(coro)
    # create the task to cancel the previous task
    asyncio.create_task(cancel_task(shielded))
    # handle cancellation
    try:
        # await the shielded task
        result = await shielded
        # report the result
        print(f'>got: {result}')
    except asyncio.CancelledError:
        print('shielded was cancelled')
    # get all tasks
    tasks = asyncio.all_tasks()
    # wait a moment
    await asyncio.sleep(1)
    # report the details of the tasks
    print(f'shielded: {shielded}')
    # report the task for the coroutine
    for task in tasks:
        if task.get_coro() is coro:
            print(f'task: {task}')

# start the asyncio event loop
asyncio.run(main())
