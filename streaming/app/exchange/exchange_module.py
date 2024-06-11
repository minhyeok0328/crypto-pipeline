from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

from app.app_container import AppContainer
from app.exchange import ByBit

class ExchangeModule(containers.DeclarativeContainer):
    bybit = providers.Singleton(ByBit)
    
    def __init__(self, kafka_service_factory, **args) -> None:
        print('kafka_service_factory: ', kafka_service_factory)
        # super().__init__(**args)

        # kafka_service = kafka_service_factory(topic='bybiy')

        # self.bybit.override(
        #     providers.Singleton(
        #         ByBit,
        #         kafka_service=kafka_service
        #     )
        # )