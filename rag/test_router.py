from router import QueryRouter


router = QueryRouter()


questions = [
    "What was the average temperature of S01?",
    "Have we seen similar temperature anomalies before?",
    "Why did S01 suddenly become hotter yesterday?",
    "What is the battery level of S02?",
    "What unusual events happened to S03?",
]


for question in questions:

    route = router.route(question)

    print(f"Question: {question}")
    print(f"Route: {route}")
    print("-" * 70)
