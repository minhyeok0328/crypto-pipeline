FROM python:3.11.9

WORKDIR /usr/src/crypto-pipeline/streaming

# intellij의 remove developerment 기능을 사용하기 위해서는 아래 패키지를 설치해야 한다. (gui application의 호환을 위해 설치해야 함)
# libxext6 libxrender1 libxtst6 libxi6 libfreetype6 < 요거

RUN apt-get update && apt-get install -y curl git
RUN pip install -r requirements.txt

# CMD [ "python", "main.py" ]