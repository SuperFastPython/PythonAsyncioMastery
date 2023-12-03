# SuperFastPython.com
# example of calling a coroutine directly
import asyncio

# define a coroutine
async def custom_coroutine():
	# report a message
    print('Hello world')

# create the coroutine and assign it to a variable
coro = custom_coroutine() # warning
