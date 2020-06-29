import asyncio
import json
import websockets

async def hello():    
    uri = 'ws://localhost:8765'
    for i in range(3):
        async with websockets.connect(uri) as websocket:
            msg = {'name': f'Rico {i}', 'note': 'hi'}
            msg_str = json.dumps(msg)

            await websocket.send(msg_str)
            print(f'> {msg}')

            greeting = await websocket.recv()
            print(f'< {greeting}')
        await asyncio.sleep(1)

asyncio.get_event_loop().run_until_complete(hello())