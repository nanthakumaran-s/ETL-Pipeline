from py_dotenv import read_dotenv
from producer import Producer
import os
import tweepy
from datetime import datetime

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
read_dotenv(dotenv_path)

bearer_token = os.getenv("BEARER_TOKEN")

producer = Producer("Tweets_Topic", "localhost:9092")


class TweetStream(tweepy.StreamingClient):
    newTweet = {}

    def on_connect(self):
        print("Connected to Twitter API")

    def on_includes(self, data):
        try:
            self.newTweet["tweet"] = data["tweets"][0].text
            self.newTweet["username"] = data["users"][0].username
            self.newTweet["created_at"] = datetime.now().strftime("%H:%M:%S")
            producer.send(self.newTweet)
        except Exception as e:
            print(e)


def main():
    query = "google lang:en"
    stream = TweetStream(bearer_token)
    stream.add_rules(tweepy.StreamRule(query))
    print(stream.get_rules())
    stream.filter(
        tweet_fields=["created_at", "author_id", "lang", "geo"],
        expansions=["author_id", "referenced_tweets.id", "geo.place_id"],
        user_fields=["username", "name"],
        place_fields=[
            "id",
            "country",
            "geo",
            "country_code",
            "name",
            "place_type",
            "full_name",
        ],
    )


if __name__ == "__main__":
    main()
