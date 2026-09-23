from .ollama_client import OllamaClient


llm = OllamaClient()

answer = llm.generate(
    "What is the capital of France?"
)

print("\nAnswer:")
print(answer)
