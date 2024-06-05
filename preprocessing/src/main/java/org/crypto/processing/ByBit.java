package org.crypto.processing;

import org.crypto.kafka.KafkaConsumerFactory;
import org.crypto.kafka.KafkaConsumerService;

public class ByBit {
    private static KafkaConsumerFactory kafkaConsumerFactory;
    private KafkaConsumerService kafkaConsumerService;

    public ByBit() {
        this.kafkaConsumerService = KafkaConsumerFactory.createKafkaConsumerService("ByBit");
    }

    public void start() {
        kafkaConsumerService.consume();
    }
}
