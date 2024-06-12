import os
from dotenv import load_dotenv

load_dotenv()

EXCHANGE_URI: dict = {
    'BYBIT_TEST_URI': os.getenv('BYBIT_TEST_URI'),
    'BYBIT_URI': os.getenv('BYBIT_URI'),
    'UPBIT_URI': os.getenv('UPBIT_URI')
}
