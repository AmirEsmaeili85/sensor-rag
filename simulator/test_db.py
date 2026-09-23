import psycopg

conn = psycopg.connect(
    host="localhost",
    port=5433,
    dbname="sensor_rag",
    user="sensor_user",
    password="sensor_password",
)

print("Connected to PostgreSQL!")

with conn.cursor() as cur:
    cur.execute("SELECT COUNT(*) FROM sensors;")
    count = cur.fetchone()[0]
    print(f"Number of sensors: {count}")

conn.close()
