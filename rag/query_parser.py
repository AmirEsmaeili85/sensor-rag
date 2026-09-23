import re


class QueryParser:

    def parse(self, question):

        question_lower = question.lower()

        # -------------------------
        # Sensor ID
        # -------------------------

        sensor_match = re.search(r"\bs\d+\b", question_lower)

        sensor_id = None

        if sensor_match:
            sensor_id = sensor_match.group(0).upper()

        # -------------------------
        # Metric
        # -------------------------

        metric = None

        if "temperature" in question_lower:
            metric = "temperature"

        elif "humidity" in question_lower:
            metric = "humidity"

        elif "pressure" in question_lower:
            metric = "pressure"

        elif "battery" in question_lower:
            metric = "battery"

        # -------------------------
        # Operation
        # -------------------------

        operation = None

        if "average" in question_lower or "mean" in question_lower:
            operation = "average"

        elif "maximum" in question_lower or "highest" in question_lower:
            operation = "maximum"

        elif "minimum" in question_lower or "lowest" in question_lower:
            operation = "minimum"

        elif "count" in question_lower or "how many" in question_lower:
            operation = "count"

        return {
            "operation": operation,
            "metric": metric,
            "sensor_id": sensor_id,
        }
