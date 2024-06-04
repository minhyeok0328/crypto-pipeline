package com.crypto.streaming;

import com.crypto.streaming.exchange.ByBit;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class StreamingApplication {
	public static void main(String[] args) {
		SpringApplication.run(StreamingApplication.class, args);
	}

	@Bean
	public CommandLineRunner run(ByBit byBit) {
		return args -> {
			byBit.start();
		};
	}
}
