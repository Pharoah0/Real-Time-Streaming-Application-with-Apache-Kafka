# Installing our Packages
from kafka import KafkaConsumer
from time import sleep
from json import dumps, loads
import json
from s3fs import S3FileSystem

# Connecting Kafka-python to bootstrap servers
consumer = KafkaConsumer(
    'MSKTopic',
    bootstrap_servers=['<<bootstrap server address 1>>','<<bootstrap server address 2>>','<<bootstrap server address 3>>'], # Need IP of MSK Cluster
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Connecting to S3 & sending data
s3 = S3FileSystem()
for count, i in enumerate(consumer):
    with s3.open("s3://kafka-project5/stock_market_data/stock_market_{}.json".format(count), 'w') as file:
        json.dump(i.value, file)