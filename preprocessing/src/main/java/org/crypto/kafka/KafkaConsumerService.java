package org.crypto.kafka;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.crypto.config.KafkaConsumerConfig;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Collections;
import java.util.Properties;

public class KafkaConsumerService {
    private static KafkaConsumer kafkaConsumer;
    private static final Logger logger = LoggerFactory.getLogger(KafkaConsumerService.class);

    public KafkaConsumerService(KafkaConsumerConfig config, String topic) {
        Properties properties = config.getProperties();
        kafkaConsumer = new KafkaConsumer<>(properties);
        kafkaConsumer.subscribe(Collections.singleton(topic));
    }

    public void consume() {
        try {
            while (true) {
                ConsumerRecords<String, String> records = kafkaConsumer.poll(100);

                for (ConsumerRecord<String, String> record : records) {
                    System.out.println(record.value());
                    logger.info(record.value());
                }
            }
        } catch (Exception e) {
            System.out.println("error: " + e);
        } finally {
            kafkaConsumer.close();
        }
    }
}
