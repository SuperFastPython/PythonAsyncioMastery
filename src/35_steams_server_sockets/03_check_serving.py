# SuperFastPython.com
# example of checking if a server is serving
import asyncio

# handler for client connections
async def handler(reader, writer):
    pass

# main coroutine
async def main():
    # create an asyncio server
    server = await asyncio.start_server(
        handler, '127.0.0.1', port=8888,
        start_serving=False)
    # report the details of the server
    print(server)
    # check if it is serving
    print(f'Serving: {server.is_serving()}')
    # start serving
    await server.start_serving()
    # check if it is serving
    print(f'Serving: {server.is_serving()}')

# start the asyncio event loop
asyncio.run(main())
