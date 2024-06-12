from app.abstract import Exchange
from app.config.exchange_config import EXCHANGE_URI

class UpBitExchange(Exchange):
    def __init__(self, kafka_service_factory, websocket_service_factory) -> None:
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
            ]
        )
