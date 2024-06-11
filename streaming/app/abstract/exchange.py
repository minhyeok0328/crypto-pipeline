from abc import ABC

class Exchange(ABC):
    def __init__(self, kafka_service_factory, websocket_service_factory, subscription_data: dict, topic: str, exchange_uri: str) -> None:
        self.kafka_service = kafka_service_factory(topic)
        self.websocket_service = websocket_service_factory(exchange_uri)
        self.subscription_data = subscription_data
        self._is_connected = True

    @property
    def is_connected(self) -> bool:
        return self._is_connected

    @is_connected.setter
    def is_connected(self, new_property: bool) -> None:
        self._is_connected = new_property

    async def run(self) -> None:
        await self.websocket_service.connect()
        await self.websocket_service.subscription(
            subscription_data=self.subscription_data
        )

        while self.is_connected:
            bybit_message: object = await self.websocket_service.receive_message(continuous=True)
            self.kafka_service.send_message(message=bybit_message)

    def disconnect(self):
        self.is_connected = False
