# SuperFastPython.com
# example of creating a subprocess with shell
import asyncio

# main coroutine
async def main():
    # create as a subprocess with shell
    process = await asyncio.create_subprocess_shell(
        'echo Hello World')
    # report the details of the subprocess
    print(f'subprocess: {process}')

# start the asyncio event loop
asyncio.run(main())
