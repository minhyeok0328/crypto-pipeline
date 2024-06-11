import json
from websockets import connect, WebSocketClientProtocol

class WebSocketService:
    uri: str
    ws: WebSocketClientProtocol

    def __init__(self, uri: str) -> None:
        self.uri = uri

    async def connect(self) -> None:
        self.ws = await connect(self.uri)
    
    async def subscription(self) -> None:
        ## 여기 데이터는 추후 따로 뺄거임
        await self.ws.send(json.dumps({
            "req_id": "test",
            "op": "subscribe",
            "args": [
                "orderbook.1.BTCUSDT",
                "publicTrade.BTCUSDT",
                "orderbook.1.ETHUSDT"
            ]
        }))

    async def receive_message(self, continuous: bool = True) -> object:
        if self.ws is None:
            raise RuntimeError('WebSocket 연결이 이상허이')

        if continuous:
            while True:
                message: object = await self.ws.recv()
                print(f'receive_message: {message}')

                return message
        else:
            message: object = await self.ws.recv()
            print(f'receive_message: {message}')
