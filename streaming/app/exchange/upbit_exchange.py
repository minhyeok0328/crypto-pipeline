import uuid
import jwt

from dependency_injector import providers
from app.abstract import Exchange
from app.config.exchange_config import EXCHANGE_KEY, EXCHANGE_URI
from app.kafka import KafkaService
from app.websocket import WebSocketService
from app.builder import ExchangeBuilder, ExchangeConfig


class UpBitExchange(Exchange):
    def __init__(
            self,
            kafka_service_factory: providers.Dependency[KafkaService],
            websocket_service_factory: providers.Dependency[WebSocketService]
    ) -> None:
        config = self.set_config()
        super().__init__(
            kafka_service_factory=kafka_service_factory,
            websocket_service_factory=websocket_service_factory,
            config=config
        )

    def set_config(self) -> ExchangeConfig:
        payload = {
            'access_key': EXCHANGE_KEY['UPBIT_ACCESS_KEY'],
            'nonce': str(uuid.uuid4())
        }

        jwt_token = jwt.encode(payload, EXCHANGE_KEY['UPBIT_SECRET_KEY'])
        authorization_token = 'Bearer {}'.format(jwt_token)

        return (
            ExchangeBuilder()
            .set_topic('upbit')
            .set_requests_per_minute_limit(100)
            .set_exchange_uri(EXCHANGE_URI['UPBIT_URI'])
            .set_subscription_data([
                {
                    "ticket": "test"
                },
                {
                    "type": "trade",
                    "codes": [
                        "KRW-BTC",
                        "BTC-BCH",
                        "BTC-XRP"
                    ]
                }
            ])
            .set_headers({
                'Authorization': authorization_token
            })
            .build()
        )
