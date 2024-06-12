from abc import ABC
import asyncio
from typing import Union

class Exchange(ABC):
    def __init__(
            self,
            kafka_service_factory,
            websocket_service_factory,
            subscription_data: Union[dict, list],
            topic: str,
            exchange_uri: str,
            requests_per_minute_limit: Union[int, float] = 0
        ) -> None:
        """
            거래소 추상화 클래스.

            kafka_service_factory (KafkaService): kafka producer 사용 목적.
            websocket_service_factory (WebSocketService): websocket 사용 목적
            subscription_data (Union[dict, list]): 구독 데이터.
            topic (str): kafka 데이터 보낼 topic 이름.
            exchange_uri (str): 거래소 uri.
            requests_per_minute_limit (int): 분당 요청제한 값. 기본값은 0
        """
        self.topic = topic
        self.kafka_service = kafka_service_factory(topic)
        self.websocket_service = websocket_service_factory(exchange_uri)
        self.subscription_data = subscription_data
        self._is_connected = True
        self.requests_per_minute_limit = 60 / requests_per_minute_limit

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
            self.kafka_service.send_message(message=exchange_message)

            # websocket 분당 요청제한 있어서 추가
            await asyncio.sleep(self.requests_per_minute_limit)

    def disconnect(self):
        self.is_connected = False
