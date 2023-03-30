from py_dotenv import read_dotenv
from producer import Producer
import os
from datetime import date, timedelta
import requests

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
read_dotenv(dotenv_path)

news_api_key = os.getenv("NEWS_API")

producer = Producer("News_Topic", "localhost:9092")


def main():
    try:
        BASE_URL = "https://newsapi.org/v2/everything"
        topic = "Google"
        today = date.today()
        yesterday = today - timedelta(days=1)
        params = {
            "q": topic,
            "from": yesterday,
            "to": today,
            "language": "en",
            "apiKey": news_api_key
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        articles = data["articles"]

        for article in articles:
            news = {
                "category": "news"
            }
            news["title"] = article["title"]
            news["description"] = article["description"]
            news["date_time"] = article["publishedAt"]
            news["source"] = article["source"]["name"]
            news["author"] = article["author"]
            news["url"] = article["url"]

            producer.send(news)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
