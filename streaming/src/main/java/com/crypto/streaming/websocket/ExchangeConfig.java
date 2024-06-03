package com.crypto.streaming.websocket;

import org.java_websocket.client.WebSocketClient;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;

@Component
public class ExchangeConfig {
    private static final String UPBIT_TEST_API = "wss://api.upbit.com/websocket/v1";

    @Bean
    public WebSocketClient upbitWebSocketTestClient() {
        return new CryptoWebSocketClient(UPBIT_TEST_API);
    }

    @Bean
    public WebSocketClient upbitWebSocketClient() {
        return new CryptoWebSocketClient(UPBIT_TEST_API);
    }
}
