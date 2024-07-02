import os
from dotenv import load_dotenv

load_dotenv()

EXCHANGE_URI: dict[str, str] = {
    'BYBIT_TEST_URI': os.getenv('BYBIT_TEST_URI') or '',
    'BYBIT_URI': os.getenv('BYBIT_URI') or '',
    'UPBIT_URI': os.getenv('UPBIT_URI') or '',
    'BINANCE_URI': os.getenv('BINANCE_URI') or '',
    'BINANCE_TEST_URI': os.getenv('BINANCE_TEST_URI') or '',
}

EXCHANGE_KEY: dict[str, str] = {
    'UPBIT_ACCESS_KEY': os.getenv('UPBIT_ACCESS_KEY') or '',
    'UPBIT_SECRET_KEY': os.getenv('UPBIT_SECRET_KEY') or '',
    'BYBIT_ACCESS_KEY': os.getenv('BYBIT_ACCESS_KEY') or '',
    'BINANCE_ACCESS_KEY': os.getenv('BINANCE_ACCESS_KEY') or '',
}
