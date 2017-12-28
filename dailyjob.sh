#!/usr/bin/env bash

python /home/harvee/scut/Data\ Mining/Altcoins/cassandraToS3.py &

python /home/harvee/scut/Data\ Mining/Altcoins/create_cassandra_table.py &
