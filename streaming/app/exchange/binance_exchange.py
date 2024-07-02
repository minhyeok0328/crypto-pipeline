import base64
import time
import uuid

from dependency_injector import providers
from app.abstract import Exchange
from app.builder import ExchangeConfig, ExchangeBuilder
from app.config.exchange_config import EXCHANGE_URI, EXCHANGE_KEY
from app.kafka import KafkaService
from app.websocket import WebSocketService
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def add_signature_parameter(params: dict) -> str:
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    payload = '&'.join([f'{param}={value}' for param, value in sorted(params.items())])
    signature = base64.b64encode(private_key.sign(
        payload.encode('ASCII'),
        padding.PKCS1v15(),
        hashes.SHA256()
    )).decode('ASCII')

    return signature


class BinanceExchange(Exchange):
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
        subscription_data = {
            "id": str(uuid.uuid4()),
            "method": "order.place",
            "params": {
                "symbol": "BTCUSDT",
                "side": "BUY",
                "type": "LIMIT",
                "price": "0.1",
                "quantity": "10",
                "timeInForce": "GTC",
                "timestamp": int(time.time() * 1000),
                "apiKey": EXCHANGE_KEY['BINANCE_ACCESS_KEY']
            }
        }

        subscription_data['params']['signature'] = add_signature_parameter(subscription_data)
        print(f'subscription_data: {subscription_data}')
        return (
            ExchangeBuilder()
            .set_topic('binance')
            .set_requests_per_minute_limit(100)
            .set_exchange_uri(EXCHANGE_URI['BINANCE_TEST_URI'])
            .set_subscription_data(subscription_data)
            .build()
        )

