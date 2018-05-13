import asyncio
import datetime
import random
import websockets

async def echotime(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat()
        await websocket.send(now)
        await asyncio.sleep(random.randrange(0,4))

start_server = websockets.serve(echotime, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()