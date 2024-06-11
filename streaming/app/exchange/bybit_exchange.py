from dependency_injector.wiring import inject, Provide

class ByBitExchange():
    def __init__(self, kafka_service_factory) -> None:
        self.kafka_service = kafka_service_factory('bybit')
        print(f'ByBitExchange: {self.kafka_service}')
        
    def run(self):
        print('run bybit!')
