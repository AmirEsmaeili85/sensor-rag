class PromptBuilder:

    def build(self, question, context):

        prompt = f"""
You are a helpful assistant for a sensor monitoring system.

Answer the user's question using the provided context.

If the context does not contain enough information to answer the question,
say that the available data is insufficient.

Do not invent sensor readings or events.

Context:
{context}

User question:
{question}

Answer:
""".strip()

        return prompt
