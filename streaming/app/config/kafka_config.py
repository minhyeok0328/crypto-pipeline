import os
from dotenv import load_dotenv

load_dotenv()

KAFKA_CONFIG: dict = {
    'bootstrap_servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS') # 내 라즈베리파이 ip
}