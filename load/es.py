from elasticsearch import Elasticsearch


class ES:
    def __init__(self, host) -> None:
        self.es = Elasticsearch(host)

    def put(self, data, indexName):
        try:
            self.es.index(index=indexName, document=data)
        except Exception as e:
            print(f"Error cannot put data into Elasticsearch: {e}")
