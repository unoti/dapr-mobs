import asyncio
import websockets

async def hello():    
    uri = 'ws://localhost:8765'
    for i in range(3):
        async with websockets.connect(uri) as websocket:
            name = f'Rico {i}'

            await websocket.send(name)
            print(f'> {name}')

            greeting = await websocket.recv()
            print(f'< {greeting}')
        await asyncio.sleep(1)

asyncio.get_event_loop().run_until_complete(hello())