# SuperFastPython.com
# example of creating a subprocess with
import asyncio

# main coroutine
async def main():
    # create as a subprocess
    process = await asyncio.create_subprocess_exec(
        'echo', 'Hello World')
    # report the details of the subprocess
    print(f'subprocess: {process}')

# start the asyncio event loop
asyncio.run(main())
