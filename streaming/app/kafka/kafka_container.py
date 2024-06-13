from dependency_injector import containers, providers

from app.kafka.kafka_service import KafkaService


class KafkaContainer(containers.DeclarativeContainer):
    kafka_service_factory = providers.Factory(KafkaService)
