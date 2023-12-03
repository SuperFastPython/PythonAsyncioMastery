# SuperFastPython.com
# example of terminating a subprocess
import asyncio

# main coroutine
async def main():
    # create a subprocess
    process = await asyncio.create_subprocess_shell(
        'sleep 3')
    # wait a moment
    await asyncio.sleep(1)
    # terminate the subprocess
    process.terminate()

# start the asyncio event loop
asyncio.run(main())
