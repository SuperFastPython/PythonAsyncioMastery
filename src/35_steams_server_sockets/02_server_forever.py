# SuperFastPython.com
# example of creating a server and serving forever
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
    # accept client connections forever (kill via control-c)
    await server.serve_forever()

# start the asyncio event loop
asyncio.run(main())
