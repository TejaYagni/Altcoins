#!/usr/bin/env python

from __future__ import print_function

import sys
import time
import json


from satori.rtm.client import make_client, SubscriptionMode

endpoint = "wss://open-data.api.satori.com"
appkey = "Ef8FaF5d8514b770C7ca0aDBFe4FcedF"
channel = "altcoins"

def main():
    with make_client(endpoint=endpoint, appkey=appkey) as client:
        print('Connected to Satori RTM!')

        class SubscriptionObserver(object):
            def on_subscription_data(self, data):
                for message in data['messages']:
                    print("Got message:", message['data']['network'])
                    with open("Data/"+message['data']['network']+message['data']['txid']+".json",'w') as f:
                        json.dump(message, f)


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