#!/usr/bin/env python

import asyncio
import websockets
import json
from connect4 import PLAYER1, PLAYER2, Connect4

async def handler(websocket):
    # Initialize a Connect Four game.
    game = Connect4()
    async for message in websocket:
        try:
            if game.last_player == PLAYER1:
                player = PLAYER2
            else:
                player = PLAYER1
            
            message_json = json.loads(message)
            print("Click: ")
            print("\t - Type: ", message_json["type"])
            print("\t - Column: ", message_json["column"])
            
            row = game.play(player, message_json["column"])
            # Add the event to dict
            event = {
                    "type": "play",
                    "player": player,
                    "column": message_json["column"],
                    "row": row,
                }
            
            # Send event to server
            print("Send Event:")
            print("\t - ", event)
            await websocket.send(json.dumps(event))
            if game.last_player_won:
                event = {
                    "type": "win",
                    "player": player,
                }
                await websocket.send(json.dumps(event))
        except RuntimeError as e:
            print("You can't do that. Try again...")
            print("e: ", e)
            error_message = str(e)
            event = {
                    "type": "error",
                    "message": error_message,
                }
            await websocket.send(json.dumps(event))



async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())