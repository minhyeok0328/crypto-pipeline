FROM openjdk:17-slim

WORKDIR /app

COPY . .

RUN apt update && apt install -y \
    curl \
    unzip \
    procps \
    libxext6 \
    libxrender1 \
    libxtst6 \
    libxi6 \
    libfreetype6 \
    && apt-get clean

RUN ./gradlew clean build

#CMD ["java", "-cp", "build/libs/preprocessing-1.0-SNAPSHOT.jar"]