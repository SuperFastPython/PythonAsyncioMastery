# SuperFastPython.com
# example of managing a server via context manager
import asyncio

# handler for client connections
async def handler(reader, writer):
    pass

# main coroutine
async def main():
    # create an asyncio server
    server = await asyncio.start_server(
        handler, '127.0.0.1', port=8888)
    # report the details of the server
    print(server)
    # start using the server
    async with server:
        # wait a moment
        await asyncio.sleep(2)
        # server is closed automatically
    # report the details of the server
    print(server)
    # check if it is serving
    print(f'Serving: {server.is_serving()}')

# start the asyncio event loop
asyncio.run(main())
