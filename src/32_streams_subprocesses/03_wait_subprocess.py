# SuperFastPython.com
# example of waiting for a subprocess to finish
import asyncio

# main coroutine
async def main():
    # create as a subprocess
    process = await asyncio.create_subprocess_shell(
        'sleep 3')
    # wait for the subprocess to terminate
    await process.wait()

# start the asyncio event loop
asyncio.run(main())
