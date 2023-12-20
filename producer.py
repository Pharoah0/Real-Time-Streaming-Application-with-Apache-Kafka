# Installing our Packages
import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json

# Connecting Kafka-python to bootstrap servers
producer = KafkaProducer(
    bootstrap_servers=['<<bootstrap server address 1>>','<<bootstrap server address 2>>','<<bootstrap server address 3>>'], # Need IP of MSK Cluster
    value_serializer=lambda x:
    dumps(x).encode('utf-8'))


df = pd.read_csv("/home/ec2-user/indexProcessed.csv")

# Loop function to send data
while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]# Ensures we get the correct information not nested within a dictionary as a value
    producer.send('MSKTopic', value=dict_stock)
    sleep(3)