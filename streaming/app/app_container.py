from dependency_injector import containers, providers
from app.kafka import KafkaModule, kafka_service
from app.websocket import WebSocketModule
from app.exchange import ExchangeModule

class AppContainer(containers.DeclarativeContainer):
    kafka_module = providers.Container(KafkaModule)
    websocket_module = providers.Container(WebSocketModule)
    exchange_module = providers.Container(
        ExchangeModule,
        kafka_service_factory=kafka_module.provided.kafka_service_factory
    )
