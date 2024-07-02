import asyncio
import json

from websockets import connect, WebSocketClientProtocol


class WebSocketService:
    uri: str
    ws: WebSocketClientProtocol

    def __init__(self, uri: str, headers=None, pong: int = 0) -> None:
        if headers is None:
            headers = {}

        self.uri = uri
        self.headers = headers
        self.pong = pong

    async def connect(self) -> None:
        try:
            self.ws = await connect(
                uri=self.uri,
                extra_headers=self.headers
            )
        except Exception as e:
            print(f"Websocket connection error: {e}")

    async def subscription(self, subscription_data: object) -> None:
        await self.ws.send(json.dumps(subscription_data))

    async def send_pong(self) -> None:
        while True:
            await self.ws.pong()
            await asyncio.sleep(60 * self.pong)

    async def receive_message(self, continuous: bool = True) -> object:
        if self.ws is None:
            raise RuntimeError('WebSocket 연결이 이상허이')

        if continuous:
            while True:
                message: object = await self.ws.recv()
                return message
        else:
            message: object = await self.ws.recv()
            return message

