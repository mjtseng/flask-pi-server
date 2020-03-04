# WS client example

import asyncio
import websockets
import pygame

'''
async def hello():
    uri = "ws://10.1.41.106:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")
'''

    # pygame code (for controller)
async def controller():
    pygame.init
    done = False
    pygame.joystick.init()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
            elif event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")

asyncio.get_event_loop().run_until_complete(controller())
