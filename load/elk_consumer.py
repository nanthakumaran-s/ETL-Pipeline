from es import ES
from consumer import Consumer
from json import loads

consumer = Consumer('Processed', 'localhost:9093', 'ELK_Loader')
es = ES("http://localhost:9200")


def main():
    for data in consumer.consumer:
        message = loads(data.value.decode('utf-8'))
        if message["category"] == "tweet":
            es.put(message, "tweet_index")
        if message["category"] == "news":
            es.put(message, "news_index")


if __name__ == '__main__':
    main()
