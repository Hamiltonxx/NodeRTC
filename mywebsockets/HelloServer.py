import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print("< {}".format(message))
        await websocket.send(message)
        print("> {}".format(message))
    # message = await websocket.recv()
    # print("< {}".format(message))

asyncio.get_event_loop().run_until_complete(websockets.serve(echo, "localhost", 8765))
asyncio.get_event_loop().run_forever()