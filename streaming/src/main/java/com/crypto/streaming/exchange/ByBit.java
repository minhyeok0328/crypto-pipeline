package com.crypto.streaming.exchange;

import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;
import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.PropertySource;
import org.springframework.stereotype.Component;

import java.net.URI;
import java.util.Map;
import java.util.concurrent.CountDownLatch;

@Component
@PropertySource("classpath:api.properties")
public class ByBit extends WebSocketClient {
    private final CountDownLatch latch = new CountDownLatch(1);

    public ByBit(@Value("${bybit.websocket.testuri}") String uri, Map<String, String> headers) {
        super(URI.create(uri), headers);
    }

    @Override
    public void onOpen(ServerHandshake serverHandshake) {
        latch.countDown();
    }

    @Override
    public void onMessage(String s) {
        System.out.println(s);
    }

    @Override
    public void onClose(int i, String s, boolean b) {
        System.out.println("on close");
    }

    @Override
    public void onError(Exception e) {
        System.out.println("on error: " + e);
    }

    public void start() throws InterruptedException {
        super.connect();
        latch.await();

        JSONObject params = new JSONObject();

        params.put("op", "subscribe");
        params.put("args", new String[]{
                "orderbook.1.BTCUSDT",
                "publicTrade.BTCUSDT",
                "orderbook.1.ETHUSDT"
        });

        super.send(params.toString());
    }
}
