from app.config.exchange_config import EXCHANGE_URI

class ByBitExchange():
    def __init__(self, kafka_service_factory, websocket_service_factory) -> None:
        self.kafka_service = kafka_service_factory('bybit')
        self.websocket_service = websocket_service_factory(EXCHANGE_URI['bybit-test'])
        self._is_connected = True

    @property
    def is_connected(self):
        return self._is_connected

    @is_connected.setter
    def is_connected(self, connected):
        self._is_connected = connected

    async def run(self):
        await self.websocket_service.connect()
        await self.websocket_service.subscription(
            subscription_data={
                'req_id': 'test',
                'op': 'subscribe',
                'args': [
                    'orderbook.1.BTCUSDT',
                    'publicTrade.BTCUSDT',
                    'orderbook.1.ETHUSDT'
                ]
            }
        )

        while self.is_connected:
            bybit_message: object = await self.websocket_service.receive_message(continuous=True)
            self.kafka_service.send_message(message=bybit_message)

    def disconnect(self):
        self.is_connected = False
