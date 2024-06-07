FROM mcr.microsoft.com/openjdk/jdk:17-ubuntu

WORKDIR /usr/src/crypto-pipeline/streaming

# intellij의 remove developerment 기능을 사용하기 위해서는 아래 패키지를 설치해야 한다. (gui application의 호환을 위해 설치해야 함)
# libxext6 libxrender1 libxtst6 libxi6 libfreetype6 < 요거

RUN apt-get update && apt-get install -y libxext6 libxrender1 libxtst6 libxi6 libfreetype6 curl git

RUN java -version

