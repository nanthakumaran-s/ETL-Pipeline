from kafka import KafkaConsumer
import json


class Consumer:
    def __init__(self, topic, server, group) -> None:
        self.topic = topic
        self.server = server
        self.group = group
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=[self.server],
            group_id=self.group
        )
