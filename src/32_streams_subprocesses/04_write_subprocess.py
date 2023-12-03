# SuperFastPython.com
# example of writing to a subprocess
import asyncio

# main coroutine
async def main():
    # create a subprocess
    process = await asyncio.create_subprocess_exec(
        'cat', stdin=asyncio.subprocess.PIPE)
    # write data to the subprocess
    _ = await process.communicate(b'Hello World\n')

# start the asyncio event loop
asyncio.run(main())
