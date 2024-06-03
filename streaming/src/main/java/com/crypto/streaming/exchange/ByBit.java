package com.crypto.streaming.exchange;

import com.crypto.streaming.abstracts.Exchange;
import org.java_websocket.client.WebSocketClient;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

@Component
public class ByBit implements Exchange {
    private final WebSocketClient webSocketClient;

    public ByBit(@Qualifier("byBitWebSocketClient") WebSocketClient webSocketClient) {
        this.webSocketClient = webSocketClient;
    }

    @Override
    public void start() throws InterruptedException {
        webSocketClient.connect();

        while (!webSocketClient.isOpen()) {
            Thread.sleep(100);
        }

        webSocketClient.send("{\"op\": \"subscribe\", \"args\": [\"orderbook.1.BTCUSDT\",\"publicTrade.BTCUSDT\",\"orderbook.1.ETHUSDT\"]}");
        webSocketClient.send("{\"op\": \"subscribe\", \"args\": [\"orderbook.1.BTCUSDT\",\"publicTrade.BTCUSDT\",\"orderbook.1.ETHUSDT\"]}");
    }
}
