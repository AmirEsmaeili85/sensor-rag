from .retriever import Retriever


retriever = Retriever(top_k=3)


questions = [
    "Have we seen unusual temperature increases before?",
    "What is the average temperature of S01?",
    "What is the maximum humidity of S02?",
    "What is the average temperature of S01 and have we seen unusual increases before?",
]


for question in questions:

    print("\n" + "=" * 80)
    print("QUESTION:")
    print(question)

    result = retriever.retrieve(question)

    print("\nROUTE:")
    print(result["route"])

    print("\nPARSED QUERY:")
    print(result["query"])

    print("\nRESULTS:")
    print(result["results"])
