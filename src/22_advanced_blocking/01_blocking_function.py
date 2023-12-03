# SuperFastPython.com
# example of running a blocking function call in asyncio
import time
import asyncio

# blocking function
def blocking_task():
    # report a message
    print('task is running')
    # block
    time.sleep(2)
    # report a message
    print('task is done')

# background coroutine task
async def background():
    # loop forever
    while True:
        # report a message
        print('>background task running')
        # sleep for a moment
        await asyncio.sleep(0.5)

# main coroutine
async def main():
    # run the background task
    _= asyncio.create_task(background())
    # execute the blocking call
    blocking_task()

# start the asyncio event loop
asyncio.run(main())
