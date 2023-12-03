# SuperFastPython.com
# example of canceling a running task with a message
import asyncio

# define a coroutine for a task
async def task_coroutine():
    try:
        # report a message
        print('executing the task')
        # block for a moment
        await asyncio.sleep(1)
    except asyncio.CancelledError as e:
        print(f'received request to cancel with: {e}')

# custom coroutine
async def main():
    # report a message
    print('main coroutine started')
    # create and schedule the task
    task = asyncio.create_task(task_coroutine())
    # wait a moment
    await asyncio.sleep(0.1)
    # cancel the task
    was_cancelled = task.cancel('Stop Right Now')
    # report whether the cancel request was successful
    print(f'was canceled: {was_cancelled}')
    # wait a moment
    await asyncio.sleep(0.1)
    # check the status of the task
    print(f'canceled: {task.cancelled()}')
    # report a final message
    print('main coroutine done')

# start the asyncio event loop
asyncio.run(main())
