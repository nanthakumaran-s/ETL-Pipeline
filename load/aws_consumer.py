from consumer import Consumer
from s3fs import S3FileSystem
from uuid import uuid4 as v4
from json import loads, dump

consumer = Consumer('Processed', 'localhost:9093', 'AWS_Loader')


def main():
    for data in consumer.consumer:
        message = loads(data.value.decode('utf-8'))
        s3 = S3FileSystem()
        file = ""
        if message["category"] == "tweet":
            file = "tweet/" + str(v4())
        if message["category"] == "news":
            file = "news/" + str(v4())
        with s3.open("s3://etl-pipeline-py-kafka/{}".format(file), 'w') as f:
            dump(message, f)


if __name__ == '__main__':
    main()
