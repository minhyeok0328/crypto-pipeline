from dependency_injector import containers, providers
from app.kafka import KafkaContainer
from app.websocket import WebSocketContainer
from app.exchange import ExchangeContainer


class AppContainer(containers.DeclarativeContainer):
    kafka_container: providers.Container[KafkaContainer] = providers.Container(KafkaContainer)
    websocket_container: providers.Container[WebSocketContainer] = providers.Container(WebSocketContainer)
    exchange_container: providers.Container[ExchangeContainer] = providers.Container(
        ExchangeContainer,
        kafka_service_factory=kafka_container.provided.kafka_service_factory,
        websocket_service_factory=websocket_container.provided.websocket_service_factory
    )
