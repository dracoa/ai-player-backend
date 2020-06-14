#!/usr/bin/env python

# WS server example

import asyncio
import websockets
from serial import Math

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

mathObj = Math()
result = mathObj.add(1, 2)
print(result)


start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()