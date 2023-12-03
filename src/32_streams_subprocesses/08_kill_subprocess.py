# SuperFastPython.com
# example of killing a subprocess
import asyncio

# main coroutine
async def main():
    # create a subprocess
    process = await asyncio.create_subprocess_shell(
        'sleep 3')
    # wait a moment
    await asyncio.sleep(1)
    # kill the subprocess
    process.kill()

# start the asyncio event loop
asyncio.run(main())
