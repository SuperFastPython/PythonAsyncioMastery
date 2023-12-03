# SuperFastPython.com
# example of calling a coroutine directly
import asyncio

# define a coroutine
async def custom_coroutine():
	# report a message
    print('Hello world')

# create a coroutine
custom_coroutine() # error
