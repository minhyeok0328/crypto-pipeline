import os
from dotenv import load_dotenv

load_dotenv()

EXCHANGE_URI: dict = {
    'BYBIT_TEST_URI': os.getenv('BYBIT_TEST_URI'),
    'BYBIT_URI': os.getenv('BYBIT_URI'),
    'UPBIT_URI': os.getenv('UPBIT_URI'),
    'BINANCE_URI': os.getenv('BINANCE_URI'),
}

EXCHANGE_KEY: dict = {
    'UPBIT_ACCESS_KEY': os.getenv('UPBIT_ACCESS_KEY'),
    'UPBIT_SECRET_KEY': os.getenv('UPBIT_SECRET_KEY'),
    'BYBIT_SECRET_KEY': os.getenv('BYBIT_SECRET_KEY'),
    'BYBIT_SECRET_KEY': os.getenv('BYBIT_SECRET_KEY'),
}
