from dependency_injector import containers, providers

from app.exchange.exchange_module import ExchangeModule
from app.kafka.kafka_module import KafkaModule
from app.websocket.websocket_module import WebSocketModule

class AppContainer(containers.DeclarativeContainer):
    kafka_module = providers.Container(KafkaModule)
    websocket_module = providers.Container(WebSocketModule)
    exchange_module = providers.Container(
        ExchangeModule,
        kafka_service_factory=kafka_module.kafka_service_factory
    )
