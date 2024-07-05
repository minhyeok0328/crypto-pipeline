package org.crypto.exchange;

import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.connector.kafka.source.KafkaSource;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.crypto.kafka.KafkaConfiguration;

public class BinanceExchange {
    private static final String TOPIC_NAME = "binance";
    private static final String GROUP_ID = "crypto-consumer";

    public static void Main() throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        KafkaConfiguration kafkaConfiguration = new KafkaConfiguration();
        KafkaSource<String> kafkaSource = kafkaConfiguration.setKafkaSource(TOPIC_NAME, GROUP_ID);

        env.fromSource(kafkaSource, WatermarkStrategy.noWatermarks(), "Kafka Source")
                .print();

        env.execute("Flink Kafka Consumer Example");
    }
}
