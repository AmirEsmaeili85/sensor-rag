from query_parser import QueryParser


parser = QueryParser()


questions = [
    "What was the average temperature of S01?",
    "What was the highest temperature of S02?",
    "What is the mean humidity of S03?",
    "What is the lowest pressure of S01?",
    "How many readings does S02 have?",
]


for question in questions:

    parsed = parser.parse(question)

    print("Question:")
    print(question)

    print("\nParsed:")
    print(parsed)

    print("-" * 70)
