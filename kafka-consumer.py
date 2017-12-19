#!/usr/bin/env python

from kafka import KafkaConsumer
import json
import sys

from cassandra.cluster import Cluster


cluster = Cluster()
session = cluster.connect("altcoins_keyspace")


def main():
    consumer = KafkaConsumer('altcoins')
    for msg in consumer:
        print (sys.argv)
        session.execute("INSERT INTO altcoins_keyspace.altcoins JSON '"+msg[6]+ "';")



if __name__ == '__main__':
    main()