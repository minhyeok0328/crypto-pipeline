package org.crypto.exchange;

import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.connector.kafka.source.KafkaSource;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.table.api.DataTypes;
import org.apache.flink.table.api.Schema;
import org.apache.flink.table.api.Table;
import org.apache.flink.table.api.bridge.java.StreamTableEnvironment;
import org.crypto.kafka.KafkaConfiguration;
import static org.apache.flink.table.api.Expressions.$;
import static org.apache.flink.table.api.Expressions.concat;
import org.apache.flink.table.types.AbstractDataType;

import java.util.stream.Stream;

public class BinanceExchange {
    private static final String TOPIC_NAME = "binance";
    private static final String GROUP_ID = "crypto-consumer";

    public static void Main() throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env);

        KafkaConfiguration kafkaConfiguration = new KafkaConfiguration();
        KafkaSource<String> kafkaSource = kafkaConfiguration.setKafkaSource(TOPIC_NAME, GROUP_ID);

        DataStream<String> stream = env.fromSource(kafkaSource, WatermarkStrategy.noWatermarks(), "Binance Kafka Source");

        Schema schema = Schema.newBuilder()
                .column("e", DataTypes.STRING())
                .column("E", DataTypes.BIGINT())
                .column("s", DataTypes.STRING())
                .column("p", DataTypes.STRING())
                .column("P", DataTypes.STRING())
                .column("o", DataTypes.STRING())
                .column("h", DataTypes.STRING())
                .column("l", DataTypes.STRING())
                .column("c", DataTypes.STRING())
                .column("w", DataTypes.STRING())
                .column("v", DataTypes.STRING())
                .column("q", DataTypes.INT())
                .column("O", DataTypes.BIGINT())
                .column("C", DataTypes.INT())
                .column("F", DataTypes.INT())
                .column("L", DataTypes.INT())
                .build();

        tableEnv.createTemporaryView("binance_table", stream, schema);

        tableEnv.executeSql("""
                    SELECT
                        e as event_type,
                        TO_TIMESTAMP_LTZ(E, 3) as event_time,
                        s as symbol,
                        p as price_change,
                        P as price_change_percent,
                        o as open_price,
                        h as high_price,
                        l as low_price,
                        c as last_price,
                        w as weighted_average_price,
                        v as total_traded_base_asset_volume,
                        q as total_traded_quote_assets_volume,
                        TO_TIMESTAMP_LTZ(O, 3) as statistics_open_time,
                        TO_TIMESTAMP_LTZ(C, 3) as statistics_close_time,
                        F as first_trade_id,
                        L as last_trade_id,
                        n as total_number_of_trades
                    FROM binance_table
                """).print();



        env.execute("Flink Kafka Consumer Example");
    }
}
