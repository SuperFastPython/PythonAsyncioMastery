# SuperFastPython.com
# example of a blocking cpu-bound task in a process
from concurrent.futures import ProcessPoolExecutor
import asyncio
import math

# a blocking cpu-bound task
def blocking_task():
    # report a message
    print('Task starting', flush=True)
    # block for a while
    data = [math.sqrt(i) for i in range(50000000)]
    # report a message
    print('Task done', flush=True)

# main coroutine
async def main():
    # report a message
    print('Main running the blocking task')
    # get the event loop
    loop = asyncio.get_running_loop()
    # create the executor
    exe = ProcessPoolExecutor(4)
    # schedule the function to run
    awaitable = loop.run_in_executor(exe, blocking_task)
    # report a message
    print('Main doing other things')
    # sleep a moment
    await asyncio.sleep(1)
    # await the cpu-bound task
    await awaitable
    # close the process pool
    exe.shutdown()

# protect the entry point
if __name__ == '__main__':
    # start the asyncio event loop
    asyncio.run(main())
