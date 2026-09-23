from sentence_transformers import SentenceTransformer
import psycopg


DB_CONFIG = {
    "host": "localhost",
    "port": 5433,
    "dbname": "sensor_rag",
    "user": "sensor_user",
    "password": "sensor_password",
}


model = SentenceTransformer("all-MiniLM-L6-v2")


documents = [
    {
        "sensor_id": "S01",
        "content": (
            "Sensor S01 in Room A experienced an unusual temperature "
            "increase from 22 degrees Celsius to 31 degrees Celsius "
            "over two hours. Humidity remained relatively stable."
        ),
    },
    {
        "sensor_id": "S02",
        "content": (
            "Sensor S02 in Room B showed stable temperature readings "
            "around 24 degrees Celsius during the afternoon."
        ),
    },
    {
        "sensor_id": "S03",
        "content": (
            "Sensor S03 in Room C experienced a rapid increase in "
            "temperature accompanied by a decrease in humidity."
        ),
    },
]


def main():
    conn = psycopg.connect(**DB_CONFIG)

    with conn.cursor() as cur:
        for document in documents:

            embedding = model.encode(
                document["content"]
            ).tolist()

            cur.execute(
                """
                INSERT INTO sensor_documents
                (sensor_id, content, embedding)
                VALUES (%s, %s, %s)
                """,
                (
                    document["sensor_id"],
                    document["content"],
                    embedding,
                ),
            )

    conn.commit()
    conn.close()

    print(f"Inserted {len(documents)} documents.")


if __name__ == "__main__":
    main()
