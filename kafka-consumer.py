#!/usr/bin/env python

from kafka import KafkaConsumer
import json
import sys

from cassandra.cluster import Cluster


cluster = Cluster()
session = cluster.connect("altcoins_keyspace")


def main():
    topic = sys.argv[1];
    consumer = KafkaConsumer(topic)
    for msg in consumer:
        session.execute("INSERT INTO altcoins_keyspace."+topic+" JSON '"+msg[6]+ "';")



if __name__ == '__main__':
    main()