package com.crypto.streaming.exchange;

import com.crypto.streaming.abstracts.Exchange;
import com.crypto.streaming.kafka.KafkaProducerService;
import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;
import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.PropertySource;
import org.springframework.stereotype.Component;

import java.net.URI;
import java.util.Map;
import java.util.concurrent.CountDownLatch;

@Component
@PropertySource("classpath:api.properties")
public class ByBit extends WebSocketClient implements Exchange {
    private final CountDownLatch latch = new CountDownLatch(1);

    @Autowired
    private KafkaProducerService kafkaProducerService;

    public ByBit(@Value("${bybit.websocket.uri}") String uri, Map<String, String> headers) {
        super(URI.create(uri), headers);
    }

    @Override
    public void onOpen(ServerHandshake serverHandshake) {
        latch.countDown();
    }

    @Override
    public void onMessage(String s) {
        String TOPIC = "ByBit";
        kafkaProducerService.sendMessage(TOPIC, s);
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
