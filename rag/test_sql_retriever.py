from sql_retriever import SQLRetriever


retriever = SQLRetriever()

sensor_id = "S01"

result = retriever.retrieve_average_temperature(sensor_id)


print("Sensor:", result[0])
print("Average temperature:", result[1])
