# Real-Time Streaming Application with Apache Kafka

Author: Pharoah Evelyn

<p align="center">
    <img src="https://github.com/Pharoah0/Real-Time-Streaming-Application-with-Apache-Kafka/blob/main/images/kafka_diagram.png" />
</p>

## Overview

#### This repository outlines the curation of a real-time streaming application to demonstrate the utility of Apache Kafka using a mock dataset.

## Business Problem

The stock market produces data in real-time, and our company needs to collect this data to enhance business intelligence by creating predictive analysis, monitoring stock prices, developing trading strategies, and managing risk.

## Data Preparation

I created an EC2 instance and initiated an Amazon MSK cluster to ensure data production and consumption with Apache Kafka.

On the EC2 instance, I installed Java-1.8.0 and Kafka v3.5.1 to coincide with my MSK Cluster. Once complete, Kafka was configured correctly; I used the below commands to create a topic, produce to, and consume from it:

```
Create topic:
/home/ec2-user/kafka_2.12-3.5.1/bin/kafka-topics.sh --create --bootstrap-server <<bootstrap server address>> --replication-factor 3 --partitions 1 --topic MSKTopic

List Topics:
/home/ec2-user/kafka_2.12-3.5.1/bin/kafka-topics.sh --bootstrap-server <<bootstrap server address>> --list

Produce to Topic:
/home/ec2-user/kafka_2.12-3.5.1/bin/kafka-console-producer.sh --create --bootstrap-server <<bootstrap server address>> --topic MSKTopic

Consume from Topic:
/home/ec2-user/kafka_2.12-3.5.1/bin/kafka-console-consumer.sh --create --bootstrap-server <<bootstrap server address>> --topic MSKTopic
```

## Methods Used

Once Kafka was configured correctly, I tested the producer and consumer jobs by sending some text data and seeing if it would be received as expected.

<p align="center">
    <img src="https://github.com/Pharoah0/Real-Time-Streaming-Application-with-Apache-Kafka/blob/main/images/kafka_test.png" />
</p>

I was successfully able to produce and consume data as expected!
The CLI with the black background is our producer instance, and the CLI with the blue background is our consumer instance.

Following this, I ran two Python scripts:

- One that pulled data from a CSV file originating from S3, producing rows of data to our Kafka Topic as JSON data every second.
- One that consumes the JSON data and sends each message back to an S3 folder as an individual file.

When successful, rows of JSON data will appear in S3 in real-time, which can be further analyzed for Data Analytics or Data Science.

## Ways to improve this project

One can connect Amazon MSK to Firehose to stream data directly into S3. This approach can be done by employing Kafka-Kinesis-Connector, which is a connector to be used with Kafka Connect.

One could also stream data into OpenSearch for real-time analysis and indexing.
