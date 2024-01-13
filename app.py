#!/usr/bin/env python

import asyncio
import websockets
import json
from connect4 import PLAYER1, PLAYER2, Connect4

async def handler(websocket):
    # Initialize a Connect Four game.
    game = Connect4()
    async for message in websocket:
        if game.last_player == PLAYER1:
            player = PLAYER2
        else:
            player = PLAYER1
        
        message_json = json.loads(message)
        print(message_json)
        print(message_json["column"])
        if message_json["type"] == "play":
            row = game.play(player, message_json["column"])
            # Add the event to dict
            player = PLAYER1
            event = {
                "type": "play",
                "player": player,
                "column": message_json["column"],
                "row": row,
            }
        elif message_json["type"] == "win":
            event = {
                "type": "win",
                "player": PLAYER1,
            }
    # Send event to server
    await websocket.send(json.dumps(event))


async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())