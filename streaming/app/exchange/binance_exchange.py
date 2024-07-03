import base64
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
            "method": "SUBSCRIBE",
            "params": [
                "!ticker@arr"  # 모든 시장 티커
            ],
        }

        return (
            ExchangeBuilder()
            .set_topic('binance')
            .set_subscription_data(subscription_data)
            .set_exchange_uri(EXCHANGE_URI['BINANCE_URI'] + '/ws/!ticker@arr')
            .build()
        )

    @staticmethod
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
