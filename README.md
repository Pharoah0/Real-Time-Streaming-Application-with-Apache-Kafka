# Real-Time Streaming Application with Apache Kafka

Author: Pharoah Evelyn

## Overview

#### This repository outlines the curation of a real-time streaming application to demonstrate the utility of Apache Kafka using a mock dataset

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

## Discoveries made

## Ways to improve this project

Python jobs directly on the EC2 servers.

Firehose to stream data directly into S3.

Stream data into OpenSearch for real-time analysis and indexing.

## Conclusions
