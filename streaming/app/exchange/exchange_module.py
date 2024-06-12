from dependency_injector import containers, providers
from app.exchange import ByBitExchange, UpBitExchange
from app.kafka.kafka_service import KafkaService
from app.websocket.websocket_service import WebSocketService

class ExchangeModule(containers.DeclarativeContainer):
    kafka_service_factory = providers.Dependency(KafkaService)
    websocket_service_factory = providers.Dependency(WebSocketService)

    bybit = providers.Singleton(
        ByBitExchange,
        kafka_service_factory=kafka_service_factory,
        websocket_service_factory=websocket_service_factory
    )

    upbit = providers.Singleton(
        UpBitExchange,
        kafka_service_factory=kafka_service_factory,
        websocket_service_factory=websocket_service_factory
    )
