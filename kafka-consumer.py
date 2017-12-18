#!/usr/bin/env python

from kafka import KafkaConsumer
consumer = KafkaConsumer('altcoins')
for msg in consumer:
    print(msg)