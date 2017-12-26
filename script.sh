#!/bin/bash

python cassandraToS3.py &

python create_cassandra_table.py &

bash kafka-setup.sh &

python kafka-producer.py &

python kafka-consumer.py altcoins &

python kafka-consumer.py altcoins2 &
