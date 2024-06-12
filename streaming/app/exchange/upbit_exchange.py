import uuid
import jwt

from dependency_injector import providers
from app.abstract import Exchange
from app.config.exchange_config import EXCHANGE_KEY, EXCHANGE_URI
from app.kafka import KafkaService
from app.websocket import WebSocketService

class UpBitExchange(Exchange):
    def __init__(self, kafka_service_factory: providers.Dependency[KafkaService], websocket_service_factory: providers.Dependency[WebSocketService]) -> None:
        payload = {
            'access_key': EXCHANGE_KEY['UPBIT_ACCESS_KEY'],
            'nonce': str(uuid.uuid4())
        }

        jwt_token = jwt.encode(payload, EXCHANGE_KEY['UPBIT_SECRET_KEY'])
        authorization_token = 'Bearer {}'.format(jwt_token)

        super().__init__(
            topic='ubit',
            requests_per_minute_limit=100,
            exchange_uri=EXCHANGE_URI['UPBIT_URI'],
            kafka_service_factory=kafka_service_factory,
            websocket_service_factory=websocket_service_factory,
            subscription_data=[
                {
                    "ticket":"test"
                },
                {
                    "type":"trade",
                    "codes":[
                        "KRW-BTC",
                        "BTC-BCH",
                        "BTC-XRP"
                    ]
                }
            ],
            headers={
                'Authorization': authorization_token
            }
        )
