#!/bin/bash

bash /home/harvee/scut/Data\ Mining/Altcoins/kafka-setup.sh &

python /home/harvee/scut/Data\ Mining/Altcoins/kafka-producer.py &

python /home/harvee/scut/Data\ Mining/Altcoins/kafka-consumer.py altcoins &

python /home/harvee/scut/Data\ Mining/Altcoins/kafka-consumer.py altcoins2 &
