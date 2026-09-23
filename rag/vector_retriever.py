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


class VectorRetriever:

    def __init__(self, top_k=3):
        self.top_k = top_k
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def retrieve(self, question, sensor_id=None):

        query_embedding = self.model.encode(question)

        conn = psycopg.connect(**DB_CONFIG)
        register_vector(conn)

        with conn.cursor() as cur:

            if sensor_id is None:

                cur.execute(
                    """
                    SELECT
                        id,
                        sensor_id,
                        content,
                        1 - (embedding <=> %s) AS similarity
                    FROM sensor_documents
                    ORDER BY embedding <=> %s
                    LIMIT %s;
                    """,
                    (
                        query_embedding,
                        query_embedding,
                        self.top_k,
                    ),
                )

            else:

                cur.execute(
                    """
                    SELECT
                        id,
                        sensor_id,
                        content,
                        1 - (embedding <=> %s) AS similarity
                    FROM sensor_documents
                    WHERE sensor_id = %s
                    ORDER BY embedding <=> %s
                    LIMIT %s;
                    """,
                    (
                        query_embedding,
                        sensor_id,
                        query_embedding,
                        self.top_k,
                    ),
                )

            results = cur.fetchall()

        conn.close()

        return results
