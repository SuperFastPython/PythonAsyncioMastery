# SuperFastPython.com
# example of getting the pid of a subprocess
import asyncio

# main coroutine
async def main():
    # create a subprocess
    process = await asyncio.create_subprocess_shell(
        'sleep 1')
    # report the pid
    print(process.pid)

# start the asyncio event loop
asyncio.run(main())
