# SuperFastPython.com
# example of creating a server and closing it again
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
    # wait a moment
    await asyncio.sleep(2)
    # close the server
    server.close()
    # wait for the server to close
    await server.wait_closed()
    # report the details of the server
    print(server)

# start the asyncio event loop
asyncio.run(main())
