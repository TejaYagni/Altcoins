import boto3
import datetime
from cassandra.cluster import Cluster
from bucket_details import bucket_name, path


cluster = Cluster()
session = cluster.connect("altcoins_keyspace")

date_collected = \
    datetime.datetime.today().strftime('%Y-%m-%d')


def main():
    s3 = boto3.resource('s3')
    file_name = date_collected+".csv"
    results = session.execute("select * from altcoins;")
    with open("Data/"+file_name,'w') as f:
        for result in results:
            f.write(str(result))
            #f.write(str(result.data.txid)+","+str(result.data.received_at)+","+str(result.data.network_fee)+","+str(result.data.amount_received)+","+str(result.type))
    obj = s3.Object(bucket_name, path + file_name)
    obj.put(Body=open("Data/"+file_name,'rb'))

if __name__ == '__main__':
    main()



