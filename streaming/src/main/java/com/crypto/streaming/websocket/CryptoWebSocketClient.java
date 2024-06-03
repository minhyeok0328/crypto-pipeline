package com.crypto.streaming.websocket;

import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.net.URI;

@Component
public class CryptoWebSocketClient extends WebSocketClient {
    public CryptoWebSocketClient(@Value("${upbit.websocket.uri}") String uri) {
        super(URI.create(uri));
    }

    @Override
    public void onOpen(ServerHandshake serverHandshake) {
        System.out.println("on open");
    }

    @Override
    public void onMessage(String s) {
        System.out.println("on message");
    }

    @Override
    public void onClose(int i, String s, boolean b) {
        System.out.println("on close");
    }

    @Override
    public void onError(Exception e) {
        System.out.println("on error");
    }

    @Override
    public void connect() {
        super.connect();
    }

    @Override
    public void send(String data) {
        super.send(data);
    }

    @Override
    public void close() {
        super.close();
    }
}
