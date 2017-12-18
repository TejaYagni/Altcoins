#!/usr/bin/env python

from __future__ import print_function

import sys
sys.path.insert(0,'application_key')
import application_key
import time

from satori.rtm.client import make_client, SubscriptionMode

from kafka import KafkaProducer


endpoint = "wss://open-data.api.satori.com"
channel = "altcoins"
topic = "altcoins"
producer = KafkaProducer(bootstrap_servers='localhost:9092')

def main():
    with make_client(endpoint=endpoint, appkey=application_key.appkey) as client:
        print('Connected to Satori RTM!')

        class SubscriptionObserver(object):
            def on_subscription_data(self, data):
                for message in data['messages']:
                    #print(message)
                    msg = str(message).encode()
                    print(msg)
                    producer.send(topic, msg)
                    producer.flush()

        subscription_observer = SubscriptionObserver()
        client.subscribe(
            channel,
            SubscriptionMode.SIMPLE,
            subscription_observer)

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    main()