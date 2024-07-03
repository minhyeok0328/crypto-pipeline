import asyncio

from dependency_injector import providers
from abc import ABC, abstractmethod

from app.kafka.kafka_service import KafkaService
from app.websocket.websocket_service import WebSocketService
from app.builder import ExchangeConfig


class Exchange(ABC):
    def __init__(
            self,
            kafka_service_factory: providers.Provider[KafkaService],
            websocket_service_factory: providers.Provider[WebSocketService]
    ) -> None:
        """
            kafka_service_factory (KafkaService): kafka producer 사용 목적.
            websocket_service_factory (WebSocketService): websocket 사용 목적
        """
        config = self.set_config()
        self.topic = config.topic
        self.kafka_service = kafka_service_factory(config.topic)
        self.websocket_service = websocket_service_factory(
            uri=config.exchange_uri,
            headers=config.headers
        )
        self.subscription_data = config.subscription_data
        self._is_connected = True
        self.requests_per_minute_limit = 0

        if config.requests_per_minute_limit:
            self.requests_per_minute_limit = 60 / config.requests_per_minute_limit

        print(f'kafka topic: {self.topic}, subscription_data: {self.subscription_data}, requests_per_minute_limit: {self.requests_per_minute_limit}')

    @abstractmethod
    def set_config(self) -> ExchangeConfig:
        """
            config (ExchangeConfig): 거래소 설정 builder
        """
        pass

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

        while self.is_connected is True:
            exchange_message: object = await self.websocket_service.receive_message()

            print(f'{self.topic}|message: {exchange_message}')
            await self.kafka_service.send_message(message=exchange_message)

            # websocket 분당 요청 제한 있어서 추가
            if self.requests_per_minute_limit:
                await asyncio.sleep(self.requests_per_minute_limit)

    def disconnect(self):
        self.is_connected = False
