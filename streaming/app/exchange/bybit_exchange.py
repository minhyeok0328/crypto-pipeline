from dependency_injector import providers
from app.abstract import Exchange
from app.builder import ExchangeConfig, ExchangeBuilder
from app.config.exchange_config import EXCHANGE_URI
from app.kafka import KafkaService
from app.websocket import WebSocketService


class ByBitExchange(Exchange):
    def __init__(
            self,
            kafka_service_factory: providers.Dependency[KafkaService],
            websocket_service_factory: providers.Dependency[WebSocketService]
    ) -> None:
        super().__init__(
            kafka_service_factory=kafka_service_factory,
            websocket_service_factory=websocket_service_factory
        )

    def set_config(self) -> ExchangeConfig:
        return (
            ExchangeBuilder()
            .set_topic('bybit')
            .set_requests_per_minute_limit(100)
            .set_exchange_uri(EXCHANGE_URI['BYBIT_TEST_URI'])
            .set_subscription_data({
                'req_id': 'test',
                'op': 'subscribe',
                'args': [
                    'orderbook.1.BTCUSDT',
                    'publicTrade.BTCUSDT',
                    'orderbook.1.ETHUSDT'
                ]
            })
            .build()
        )