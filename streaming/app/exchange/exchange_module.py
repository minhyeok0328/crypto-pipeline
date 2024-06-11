from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from app.exchange import ByBitExchange

class ExchangeModule(containers.DeclarativeContainer):
    kafka_service_factory = providers.Dependency()

    bybit = providers.Singleton(
        ByBitExchange,
        kafka_service_factory=kafka_service_factory
    )
