# SuperFastPython.com
# example of getting the return code of a subprocess
import asyncio

# main coroutine
async def main():
    # create a subprocess
    process = await asyncio.create_subprocess_shell(
        'sleep 1')
    # wait for the process to terminate
    await process.wait()
    # get the return code from the process
    print(process.returncode)

# start the asyncio event loop
asyncio.run(main())
