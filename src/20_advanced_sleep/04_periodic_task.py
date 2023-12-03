# SuperFastPython.com
# example of a sleep in a periodic task
import asyncio

# periodic task
async def periodic():
    # loop forever
    while True:
        # perform operation
        print('>task is running')
        # block for an interval
        await asyncio.sleep(0.2)

# entry point coroutine
async def main():
    # report a message
    print('Main is starting')
    # start the periodic task
    _ = asyncio.create_task(periodic())
    # report a message
    print('Main is resuming with work...')
    # wait a while for some reason
    await asyncio.sleep(3)
    # report a message
    print('Main is done')

# start the asyncio event loop
asyncio.run(main())
