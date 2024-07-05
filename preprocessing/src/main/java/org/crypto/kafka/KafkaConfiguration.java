package org.crypto.kafka;

import org.apache.flink.connector.kafka.source.KafkaSource;
import org.apache.flink.connector.kafka.source.reader.deserializer.KafkaRecordDeserializationSchema;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.common.serialization.StringDeserializer;
import java.util.Properties;

public class KafkaConfiguration {
    private static final String BOOTSTRAP_SERVER = "192.168.0.5:9092"; // 내 집 라즈베리파이 ip 주소 추후 변경 예정
    private static final Boolean AUTO_COMMIT = false;

    public KafkaSource<String> setKafkaSource(String topic_name, String group_id) {
        Properties properties = new Properties();
        properties.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, BOOTSTRAP_SERVER);
        properties.put(ConsumerConfig.GROUP_ID_CONFIG, group_id);
        properties.put(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, AUTO_COMMIT); // 거래데이터 손실되면 안되기 때문에 false로
        properties.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        properties.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());

        return KafkaSource
                .<String>builder()
                .setTopics(topic_name)
                .setDeserializer(KafkaRecordDeserializationSchema.valueOnly(StringDeserializer.class))
                .setProperties(properties)
                .build();
    }

}
