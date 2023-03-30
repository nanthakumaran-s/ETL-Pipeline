# ETL Pipeline for Tweets and News using Python, Kafka, AWS and ELK Stack

## Architecture of the application

![arch](assets/architecture.png)

## Running the ETL Pipeline

### Step 1: Start Kafka, Elastic Search and Kibana

Create volumes for storing the data locally, run

```sh
bash bin/createVols.sh
```

This will creat the volumes to be mounted with the contianers. Then run the following command to start the kafka brokers with the zookeeper, Elastic Search and Kibana

```sh
docker compose up
```

### Step 2: Extract

To extract data from the source, you need to run the following commands in different terminal

```sh
python3 extract/tweet_producer.py
```

```sh
python3 extract/news_producer.py
```

To check if the producer produces any data, run the following commands in different terminal

```sh
kafka-console-consumer.sh --topic Tweets_Topic --bootstrap-server localhost:9092

or

kafka-console-consumer.sh --topic News_Topic --bootstrap-server localhost:9092
```

If it produces any data then the extract part is working fine.
