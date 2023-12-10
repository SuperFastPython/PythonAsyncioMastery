# SuperFastPython.com
# example of fixed race condition with shared memory
import asyncio

# task that operates on a shared variable
async def task(lock):
    # acquire the lock
    async with lock:
        # declare global variable
        global value
        # retrieve the value
        tmp = value
        # suspend for a moment
        await asyncio.sleep(0)
        # update the tmp value
        tmp = tmp + 1
        # suspend for a moment
        await asyncio.sleep(0)
        # store the updated value
        value = tmp

# main coroutine
async def main():
    # declare the global variable
    global value
    # define the global variable
    value = 0
    # create the shared lock
    lock = asyncio.Lock()
    # create many coroutines to update the global sate
    coros = [task(lock) for _ in range(10000)]
    # execute all coroutines
    await asyncio.gather(*coros)
    # report the value of the counter
    print(value)

# entry point
asyncio.run(main())
