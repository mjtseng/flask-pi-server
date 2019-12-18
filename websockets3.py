import asyncio
import websockets
import time

async def hello(websocket, path):
    greeting = f"Hello!"
    counter = 0
    while True:
        greeting = f"Hello {counter}"
        await websocket.send(greeting)
        print(f"> {greeting}")
        time.sleep(1)
        counter += 1

start_server = websockets.serve(hello, "10.1.41.116", 8888)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
