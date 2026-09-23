class QueryRouter:

    def route(self, question):

        question_lower = question.lower()

        # Questions that usually require numerical/structured data
        sql_keywords = [
            "average",
            "mean",
            "maximum",
            "minimum",
            "max",
            "min",
            "how many",
            "count",
            "temperature",
            "humidity",
            "pressure",
            "battery",
        ]

        # Questions that usually require semantic/historical context
        vector_keywords = [
            "similar",
            "similarity",
            "unusual",
            "anomaly",
            "anomalies",
            "event",
            "events",
            "history",
            "historical",
            "previous",
            "before",
        ]

        has_sql = any(
            keyword in question_lower
            for keyword in sql_keywords
        )

        has_vector = any(
            keyword in question_lower
            for keyword in vector_keywords
        )

        if has_sql and has_vector:
            return "hybrid"

        if has_sql:
            return "sql"

        if has_vector:
            return "vector"

        return "vector"
