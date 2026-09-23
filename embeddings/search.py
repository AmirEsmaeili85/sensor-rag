from sentence_transformers import SentenceTransformer
import psycopg
from pgvector.psycopg import register_vector


DB_CONFIG = {
    "host": "localhost",
    "port": 5433,
    "dbname": "sensor_rag",
    "user": "sensor_user",
    "password": "sensor_password",
}


model = SentenceTransformer("all-MiniLM-L6-v2")


question = "Have we seen unusual temperature increases before?"

# Convert the question into a vector
query_embedding = model.encode(question)


conn = psycopg.connect(**DB_CONFIG)

# Register PostgreSQL VECTOR type
register_vector(conn)


with conn.cursor() as cur:

    cur.execute(
        """
        SELECT
            id,
            sensor_id,
            content,
            1 - (embedding <=> %s) AS similarity
        FROM sensor_documents
        ORDER BY embedding <=> %s
        LIMIT 3;
        """,
        (query_embedding, query_embedding),
    )

    results = cur.fetchall()


conn.close()


print("\nQuestion:")
print(question)

print("\nMost similar documents:\n")

for row in results:
    doc_id, sensor_id, content, similarity = row

    print(f"Document ID: {doc_id}")
    print(f"Sensor: {sensor_id}")
    print(f"Similarity: {similarity:.4f}")
    print(f"Content: {content}")
    print("-" * 80)
