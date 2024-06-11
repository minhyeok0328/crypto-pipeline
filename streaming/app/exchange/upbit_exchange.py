from dependency_injector.wiring import inject, Provide

class UpBitExchange():
    def __init__(self, kafka_service) -> None:
        self.kafka_service = kafka_service
        print(f'UpBitExchange: {kafka_service}')
        
    def run(self):
        print('run UpBit!')
