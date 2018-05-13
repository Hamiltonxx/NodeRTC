import asyncio
import websockets

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello Hamilton!")
        print("> Hello Hamilton!")
        recvmsg = await websocket.recv()
        print("< {}".format(recvmsg))

asyncio.get_event_loop().run_until_complete(hello("ws://localhost:8765"))