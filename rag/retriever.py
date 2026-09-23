from .sql_retriever import SQLRetriever
from .vector_retriever import VectorRetriever
from .router import QueryRouter
from .query_parser import QueryParser


class Retriever:

    def __init__(self, top_k=3):

        self.router = QueryRouter()
        self.parser = QueryParser()

        self.sql_retriever = SQLRetriever()
        self.vector_retriever = VectorRetriever(top_k=top_k)

    def retrieve(self, question):

        route = self.router.route(question)

        # -------------------------
        # SQL
        # -------------------------

        if route == "sql":

            query = self.parser.parse(question)

            results = self.sql_retriever.retrieve(query)

            return {
                "route": "sql",
                "query": query,
                "results": results,
            }

        # -------------------------
        # Vector
        # -------------------------

        elif route == "vector":

            results = self.vector_retriever.retrieve(question)

            return {
                "route": "vector",
                "query": None,
                "results": results,
            }

        # -------------------------
        # Hybrid
        # -------------------------

        elif route == "hybrid":

            query = self.parser.parse(question)

            sql_results = None

            if (
                query["sensor_id"] is not None
                and query["metric"] is not None
                and query["operation"] is not None
            ):
                sql_results = self.sql_retriever.retrieve(query)

            vector_results = self.vector_retriever.retrieve(question)

            return {
                "route": "hybrid",
                "query": query,
                "results": {
                    "sql": sql_results,
                    "vector": vector_results,
                },
            }

        raise ValueError(f"Unsupported route: {route}")
