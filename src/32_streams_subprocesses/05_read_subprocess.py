# SuperFastPython.com
# example of reading from a subprocess
import asyncio

# main coroutine
async def main():
    # create a subprocess
    process = await asyncio.create_subprocess_shell(
        'echo Hello World',
        stdout=asyncio.subprocess.PIPE)
    # read data from the subprocess
    data, _ = await process.communicate()
    # report the data
    print(data)

# start the asyncio event loop
asyncio.run(main())
