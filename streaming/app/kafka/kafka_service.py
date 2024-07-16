import json

from kafka import KafkaProducer
from app.config.kafka_config import KAFKA_CONFIG


class KafkaService:
    topic: str
    producer: KafkaProducer

    def __init__(self, topic: str) -> None:
        self.topic = topic
        self.producer: KafkaProducer = KafkaProducer(
            **KAFKA_CONFIG,
            value_serializer=lambda v: v if isinstance(v, bytes) else json.dumps(v).encode('utf-8'),
            acks='all'
        )

    async def send_message(self, message: object) -> None:
        test = self.producer.send(topic=self.topic, value=message)
        result = test.get(timeout=10)

        self.producer.flush()
