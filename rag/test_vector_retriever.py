from vector_retriever import VectorRetriever


retriever = VectorRetriever(top_k=3)


question = "Have we seen unusual temperature increases before?"

results = retriever.retrieve(question)


print("\nQuestion:")
print(question)

print("\nRetrieved documents:\n")

for doc_id, sensor_id, content, similarity in results:

    print(f"Document ID: {doc_id}")
    print(f"Sensor: {sensor_id}")
    print(f"Similarity: {similarity:.4f}")
    print(f"Content: {content}")
    print("-" * 80)
