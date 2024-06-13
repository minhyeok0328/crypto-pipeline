from typing import Union, Dict, List


class ExchangeConfig:
    def __init__(self, subscription_data: Union[dict, List[dict]], topic: str, exchange_uri: str,
                 requests_per_minute_limit: Union[int, float] = 0, headers: Dict[str, str] = None):
        """
                subscription_data: 구독 데이터.
                topic: kafka 데이터 보낼 topic 이름.
                exchange_uri: 거래소 uri.
                requests_per_minute_limit: 분당 요청제한 값. 기본값은 0
                headers: websocket 헤더 설정
        """
        self.subscription_data = subscription_data
        self.topic = topic
        self.exchange_uri = exchange_uri
        self.requests_per_minute_limit = requests_per_minute_limit
        self.headers = headers if headers is not None else {}


class ExchangeBuilder:
    def __init__(self) -> None:
        self.subscription_data = None
        self.topic = ''
        self.exchange_uri = ''
        self.requests_per_minute_limit = 0
        self.headers = {}

    def set_requests_per_minute_limit(self, requests_per_minute_limit: Union[int, float]):
        self.requests_per_minute_limit = requests_per_minute_limit
        return self

    def set_headers(self, headers: Dict[str, str]):
        self.headers = headers
        return self

    def set_exchange_uri(self, exchange_uri: str):
        self.exchange_uri = exchange_uri
        return self

    def set_topic(self, topic: str):
        self.topic = topic
        return self

    def set_subscription_data(self, subscription_data: Union[dict, list]):
        self.subscription_data = subscription_data
        return self

    def build(self):
        return ExchangeConfig(
            subscription_data=self.subscription_data,
            topic=self.topic,
            exchange_uri=self.exchange_uri,
            requests_per_minute_limit=self.requests_per_minute_limit,
            headers=self.headers
        )