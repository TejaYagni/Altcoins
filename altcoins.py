#!/usr/bin/env python

from __future__ import print_function

import sys
sys.path.insert(0,'application_key')
import application_key
import time
import json


from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect("altcoins_keyspace")



from satori.rtm.client import make_client, SubscriptionMode

endpoint = "wss://open-data.api.satori.com"
channel = "altcoins"

def main():
    with make_client(endpoint=endpoint, appkey=application_key.appkey) as client:
        session.execute("INSERT INTO abc(val, val2) values (2,'king');")
        print('Connected to Satori RTM!')

        class SubscriptionObserver(object):
            def on_subscription_data(self, data):
                for message in data['messages']:
                    print("Got message:", message['data']['network'])
                    '''
                    session.execute("INSERT INTO altcoins("
                                    " txid, "
                                    " data.network, "
                                    " data.txid, "
                                    " data.received_at, "
                                    " data.network_fee, "
                                    " data.amount_received, "
                                    " data.inputs, "
                                    " data.outputs ) "
                                    "values "
                                    "( "
                                    +message['data']['txid'] + \
                                    +message['data']['network'] \
                                    +message['data']['txid'] \
                                    +message['data']['received_at'] \
                                    +message['data']['network_fee'] \
                                    +message['data']['amount_received'] \
                                    +message['data']['inputs'] \
                                    +message['data']['outputs']
                                    +");"
                                    )
'''

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