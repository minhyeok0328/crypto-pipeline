package org.crypto.kafka;

import org.crypto.config.KafkaConsumerConfig;

public class KafkaConsumerFactory {
    private static final KafkaConsumerConfig kafkaConsumerConfig = new KafkaConsumerConfig();

    public static KafkaConsumerService createKafkaConsumerService(String topic) {
        return new KafkaConsumerService(kafkaConsumerConfig, topic);
    }
}
