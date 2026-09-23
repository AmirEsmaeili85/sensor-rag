import psycopg


DB_CONFIG = {
    "host": "localhost",
    "port": 5433,
    "dbname": "sensor_rag",
    "user": "sensor_user",
    "password": "sensor_password",
}


class SQLRetriever:

    def retrieve(self, query):

        sensor_id = query["sensor_id"]
        metric = query["metric"]
        operation = query["operation"]

        allowed_metrics = {
            "temperature",
            "humidity",
            "pressure",
            "battery",
        }

        allowed_operations = {
            "average": "AVG",
            "maximum": "MAX",
            "minimum": "MIN",
        }

        if metric not in allowed_metrics:
            raise ValueError(f"Unsupported metric: {metric}")

        if operation not in allowed_operations:
            raise ValueError(f"Unsupported operation: {operation}")

        sql_operation = allowed_operations[operation]

        sql = f"""
            SELECT
                sensor_id,
                {sql_operation}({metric}) AS result
            FROM sensor_readings
            WHERE sensor_id = %s
            GROUP BY sensor_id;
        """

        conn = psycopg.connect(**DB_CONFIG)

        with conn.cursor() as cur:

            cur.execute(
                sql,
                (sensor_id,)
            )

            result = cur.fetchone()

        conn.close()

        return result
