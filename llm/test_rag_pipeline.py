from .fake_llm import FakeLLM
from .prompt_builder import PromptBuilder
from rag.context_builder import ContextBuilder


question = "Have we seen unusual temperature increases before?"

retrieved_results = [
    (
        1,
        "S01",
        (
            "Sensor S01 experienced an unusual temperature "
            "increase from 22 degrees Celsius to 31 degrees "
            "Celsius over two hours."
        ),
        0.82,
    ),
    (
        2,
        "S02",
        (
            "Sensor S02 showed stable temperature readings "
            "around 24 degrees Celsius."
        ),
        0.61,
    ),
]


# Step 1: Build context
context_builder = ContextBuilder()

context = context_builder.build(
    route="vector",
    results=retrieved_results,
)


# Step 2: Build prompt
prompt_builder = PromptBuilder()

prompt = prompt_builder.build(
    question=question,
    context=context,
)


# Step 3: Send prompt to LLM
llm = FakeLLM()

answer = llm.generate(prompt)


print("\nQUESTION:")
print(question)

print("\nCONTEXT:")
print(context)

print("\nPROMPT:")
print(prompt)

print("\nANSWER:")
print(answer)
