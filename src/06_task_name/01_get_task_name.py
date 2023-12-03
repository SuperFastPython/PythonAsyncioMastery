# SuperFastPython.com
# example of getting the default task name
import asyncio

# define a coroutine for a task
async def task_coroutine():
    # report a message
    print('executing the task')
    # block for a moment
    await asyncio.sleep(1)

# custom coroutine
async def main():
    # report a message
    print('main coroutine started')
    # create and schedule the task
    task = asyncio.create_task(task_coroutine())
    # wait for the task to complete
    await task
    # report the task
    print(task)
    # report the task name
    print(f'name: {task.get_name()}')
    # report a final message
    print('main coroutine done')

# start the asyncio event loop
asyncio.run(main())
