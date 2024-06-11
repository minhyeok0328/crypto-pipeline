from app.abstract import Exchange
from app.config.exchange_config import EXCHANGE_URI

class ByBitExchange(Exchange):
    def __init__(self, kafka_service_factory, websocket_service_factory) -> None:
        super().__init__(
            topic='bybit',
            exchange_uri=EXCHANGE_URI['BYBIT_TEST_URI'],
            kafka_service_factory=kafka_service_factory,
            websocket_service_factory=websocket_service_factory,
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
