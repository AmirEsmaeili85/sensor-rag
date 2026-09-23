from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")

text = """
Sensor S01 in Room A experienced an unusual temperature increase
from 22 degrees Celsius to 31 degrees Celsius over two hours.
Humidity remained relatively stable during this period.
"""

embedding = model.encode(text)

print("Embedding type:", type(embedding))
print("Embedding dimension:", len(embedding))
print("First 10 values:", embedding[:10])
