from query_parser import QueryParser
from sql_retriever import SQLRetriever


parser = QueryParser()
retriever = SQLRetriever()


question = "What was the average temperature of S01?"


parsed_query = parser.parse(question)

print("Parsed query:")
print(parsed_query)


result = retriever.retrieve(parsed_query)

print("\nDatabase result:")
print(result)
