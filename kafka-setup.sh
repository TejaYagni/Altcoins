#!/usr/bin/env bash
# start zookeeper
 /home/harvee/zookeeper-3.3.6/bin/zkServer.sh start > /tmp/zookeeper.logs &

#Start the kafka server
 /home/harvee/kafka_2.12-0.11.0.2/bin/kafka-server-start.sh /home/harvee/kafka_2.12-0.11.0.2/config/server.properties > /tmp/kafka_server.logs &

# Create a kafka topic
 /home/harvee/kafka_2.12-0.11.0.2/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic altcoins
 /home/harvee/kafka_2.12-0.11.0.2/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic altcoins2