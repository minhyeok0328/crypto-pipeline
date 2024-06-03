package com.crypto.streaming.exchange;

import org.java_websocket.client.WebSocketClient;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

@Component
public class UPBit {
    private final WebSocketClient webSocketClient;

    public UPBit(@Qualifier("upbitWebSocketClient") WebSocketClient webSocketClient) {
        this.webSocketClient = webSocketClient;
    }

    public void start() {
        webSocketClient.connect();
//        webSocketClient.send("[{'ticket':'test'},{'type':'ticker','codes':['KRW-BTC']}]");
    }
}
