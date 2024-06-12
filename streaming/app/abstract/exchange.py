import asyncio

from dependency_injector import providers
from abc import ABC
from typing import Union

from app.kafka.kafka_service import KafkaService
from app.websocket.websocket_service import WebSocketService

class Exchange(ABC):
    def __init__(
            self,
            kafka_service_factory: providers.Provider[KafkaService],
            websocket_service_factory: providers.Provider[WebSocketService],
            subscription_data: Union[dict, list],
            topic: str,
            exchange_uri: str,
            requests_per_minute_limit: Union[int, float] = 0,
            headers: dict[str, str] = {}
        ) -> None:
        """
            kafka_service_factory (KafkaService): kafka producer 사용 목적.
            websocket_service_factory (WebSocketService): websocket 사용 목적
            subscription_data (Union[dict, list]): 구독 데이터.
            topic (str): kafka 데이터 보낼 topic 이름.
            exchange_uri (str): 거래소 uri.
            requests_per_minute_limit (int): 분당 요청제한 값. 기본값은 0
            headers (dict): websocket 헤더 설정
        """
        self.topic = topic
        self.kafka_service = kafka_service_factory(topic)
        self.websocket_service = websocket_service_factory(
            uri=exchange_uri,
            headers=headers
        )
        self.subscription_data = subscription_data
        self._is_connected = True
        self.requests_per_minute_limit = 60 / requests_per_minute_limit

        print(f'kafka topic: {topic}, subscription_data: {subscription_data}, requests_per_minute_limit: {self.requests_per_minute_limit}')

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

            # websocket 분당 요청제한 있어서 추가
            if self.requests_per_minute_limit:
                await asyncio.sleep(self.requests_per_minute_limit)

    def disconnect(self):
        self.is_connected = False
