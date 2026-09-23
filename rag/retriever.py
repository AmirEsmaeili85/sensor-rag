from sql_retriever import SQLRetriever
from vector_retriever import VectorRetriever
from router import QueryRouter


class Retriever:

    def __init__(self):

        self.router = QueryRouter()
        self.sql_retriever = SQLRetriever()
        self.vector_retriever = VectorRetriever(top_k=3)

    def retrieve(self, question):

        route = self.router.route(question)

        if route == "sql":

            # Temporary example
            results = self.sql_retriever.retrieve_average_temperature("S01")

            return {
                "route": "sql",
                "results": results,
            }

        elif route == "vector":

            results = self.vector_retriever.retrieve(question)

            return {
                "route": "vector",
                "results": results,
            }

        else:

            return {
                "route": "hybrid",
                "results": None,
            }
