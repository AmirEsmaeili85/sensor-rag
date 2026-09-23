import random
from datetime import datetime, timezone

import psycopg


DB_CONFIG = {
    "host": "localhost",
    "port": 5433,
    "dbname": "sensor_rag",
    "user": "sensor_user",
    "password": "sensor_password",
}


def generate_reading(sensor_id):
    return {
        "sensor_id": sensor_id,
        "timestamp": datetime.now(timezone.utc),
        "temperature": round(random.uniform(20, 30), 2),
        "humidity": round(random.uniform(35, 65), 2),
        "pressure": round(random.uniform(990, 1030), 2),
        "battery": round(random.uniform(70, 100), 2),
    }


def insert_reading(conn, reading):
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO sensor_readings
            (sensor_id, timestamp, temperature, humidity, pressure, battery)
            VALUES
            (%(sensor_id)s, %(timestamp)s, %(temperature)s,
             %(humidity)s, %(pressure)s, %(battery)s)
            """,
            reading,
        )

    conn.commit()


def main():
    sensors = ["S01", "S02", "S03"]

    conn = psycopg.connect(**DB_CONFIG)

    for sensor_id in sensors:
        reading = generate_reading(sensor_id)
        insert_reading(conn, reading)
        print(reading)

    conn.close()


if __name__ == "__main__":
    main()
