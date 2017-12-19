#!/usr/bin/env bash
#Move to zookeeper directory and then use this command
sudo su
cd
cd zookeeper-3.3.6
bin/zkServer.sh start > /tmp/zookeeper.logs &

#Move to Kafka directory and then use this command
cd
cd kafka_2.12-0.11.0.2/

#Start the kafka server
bin/kafka-server-start.sh config/server.properties > tmp/kafka_server.logs &

# Create a kafka topic
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic altcoins
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic altcoins2