package com.crypto.streaming.config;

import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;

import java.net.URI;
import java.util.Map;

public class CryptoWebSocketClient extends WebSocketClient {
    public CryptoWebSocketClient(String uri, Map<String, String> headers) {
        super(URI.create(uri), headers);
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
