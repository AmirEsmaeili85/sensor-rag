class ContextBuilder:

    def build(self, route, results):

        if route == "vector":
            return self._build_vector_context(results)

        elif route == "sql":
            return self._build_sql_context(results)

        elif route == "hybrid":
            return self._build_hybrid_context(results)

        raise ValueError(f"Unsupported route: {route}")

    def _build_vector_context(self, results):

        if not results:
            return "No relevant documents were found."

        context_parts = []

        for doc_id, sensor_id, content, similarity in results:

            context_parts.append(
                f"""Document ID: {doc_id}
Sensor: {sensor_id}
Similarity: {similarity:.4f}
Content: {content}"""
            )

        return "\n\n".join(context_parts)

    def _build_sql_context(self, results):

        if not results:
            return "No structured data was found."

        sensor_id, value = results

        return (
            f"Sensor: {sensor_id}\n"
            f"Structured result: {value}"
        )

    def _build_hybrid_context(self, results):

        sql_results = results.get("sql")
        vector_results = results.get("vector")

        context_parts = []

        # SQL context
        if sql_results:
            sensor_id, value = sql_results

            context_parts.append(
                f"""Structured data:
Sensor: {sensor_id}
Result: {value}"""
            )
        else:
            context_parts.append(
                "Structured data:\nNo structured data was found."
            )

        # Vector context
        if vector_results:
            vector_context = self._build_vector_context(vector_results)

            context_parts.append(
                f"Semantic/event data:\n{vector_context}"
            )
        else:
            context_parts.append(
                "Semantic/event data:\n"
                "No relevant documents were found."
            )

        return "\n\n".join(context_parts)
