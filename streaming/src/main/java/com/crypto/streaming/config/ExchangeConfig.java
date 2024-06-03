package com.crypto.streaming.config;

import org.java_websocket.client.WebSocketClient;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import java.util.HashMap;
import java.util.Map;

@Configuration
@PropertySource("classpath:api.properties")
public class ExchangeConfig {
    @Value("${upbit.websocket.uri}")
    private String upBitApiUri;

    @Value("${upbit.api_key}")
    private String upBitApiKey;

    @Value("${bybit.websocket.testuri}")
    private String byBitApiTestUri;

    @Bean
    public WebSocketClient upBitWebSocketClient() {
        Map<String, String> requestHeaders = new HashMap<>();
        requestHeaders.put("Authorization", "Baerer " + upBitApiKey);

        return new CryptoWebSocketClient(upBitApiUri, requestHeaders);
    }

    @Bean
    public WebSocketClient byBitWebSocketClient() {
        Map<String, String> requestHeaders = new HashMap<>();
        return new CryptoWebSocketClient(byBitApiTestUri, requestHeaders);
    }
}
