from rag.retriever import Retriever
from rag.context_builder import ContextBuilder
from .prompt_builder import PromptBuilder
from .ollama_client import OllamaClient


retriever = Retriever(top_k=3)
context_builder = ContextBuilder()
prompt_builder = PromptBuilder()
llm = OllamaClient()


questions = [
    "Have we seen unusual temperature increases before?",
    "What is the average temperature of S01?",
    "What is the average temperature of S01 and have we seen unusual increases before?",
]


for question in questions:

    print("\n" + "=" * 80)

    print("QUESTION:")
    print(question)

    # 1. Retrieve
    retrieved = retriever.retrieve(question)

    print("\nROUTE:")
    print(retrieved["route"])

    # 2. Build context
    context = context_builder.build(
        route=retrieved["route"],
        results=retrieved["results"],
    )

    print("\nCONTEXT:")
    print(context)

    # 3. Build prompt
    prompt = prompt_builder.build(
        question=question,
        context=context,
    )

    # 4. Generate answer using Qwen
    answer = llm.generate(prompt)

    print("\nANSWER:")
    print(answer)
