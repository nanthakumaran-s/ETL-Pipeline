from producer import Producer
from consumer import Consumer
from textblob import TextBlob
from json import loads

producer = Producer("Processed", "localhost:9093")
consumer = Consumer("Tweets_Topic", "localhost:9092", "Tweet_Processing_Group")


def main():
    try:
        for data in consumer.consumer:
            tweet = loads(data.value.decode('utf-8'))
            blob = TextBlob(tweet["tweet"])
            polarity = blob.sentiment.polarity
            if polarity > 0:
                tweet["sentiment"] = 'positive'
            elif polarity < 0:
                tweet["sentiment"] = 'negative'
            elif polarity == 0:
                tweet["sentiment"] = 'neutral'
            producer.send(tweet)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
