print('Wolf Server 0.1')

import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f'< {name}')

    greeting = f'Hello, {name}!'

    await websocket.send(greeting)
    print(f'> {greeting}')

# Workaround to make ctrl-C work on Windows.
# https://stackoverflow.com/questions/27480967/why-does-the-asyncios-event-loop-suppress-the-keyboardinterrupt-on-windows
async def wakeup():
    while True:
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
start_server = websockets.serve(hello, 'localhost', 8765)
loop.run_until_complete(start_server)

# Windows interrupt workaround
loop.create_task(wakeup())

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

