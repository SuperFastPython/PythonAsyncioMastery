# SuperFastPython.com
# example of sending a signal to a subprocess
import asyncio
import signal

# main coroutine
async def main():
    # create a subprocess
    process = await asyncio.create_subprocess_shell(
        'sleep 3')
    # wait a moment
    await asyncio.sleep(1)
    # send a signal to the process
    process.send_signal(signal.SIGKILL)

# start the asyncio event loop
asyncio.run(main())
