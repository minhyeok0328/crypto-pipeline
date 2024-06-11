from dependency_injector.wiring import inject, Provide

from app.kafka.kafka_service import KafkaService

class ByBit():

    @inject
    def __init__(self, kafka_service: KafkaService) -> None:
        self.kafka_service = kafka_service
