package com.crypto.streaming.config;

import com.crypto.streaming.exchange.ByBit;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import java.util.HashMap;
import java.util.Map;

@Configuration
@PropertySource("classpath:api.properties")
public class ExchangeConfig {

    @Bean
    public ByBit byBit(@Value("${bybit.websocket.testuri}") String uri) {
        Map<String, String> requestHeaders = new HashMap<>();

        return new ByBit(uri, requestHeaders);
    }
}
