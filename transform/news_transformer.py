from producer import Producer
from consumer import Consumer
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from json import loads

producer = Producer("Processed", "localhost:9093")
consumer = Consumer("News_Topic", "localhost:9092", "News_Processing_Group")


def main():
    try:
        for data in consumer.consumer:
            news = loads(data.value.decode('utf-8'))
            blob = TextBlob(news["description"], analyzer=NaiveBayesAnalyzer())
            p_pos = blob.sentiment.p_pos
            p_neg = blob.sentiment.p_neg
            if p_pos > p_neg:
                news["sentiment"] = 'positive'
            elif p_pos < p_neg:
                news["sentiment"] = 'negative'
            elif p_pos == p_neg:
                news["sentiment"] = 'neutral'
            producer.send(news)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
