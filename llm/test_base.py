from base import LLM


class FakeLLM(LLM):

    def generate(self, prompt: str) -> str:
        return f"Fake answer for: {prompt}"


llm = FakeLLM()

answer = llm.generate("What is the average temperature of S01?")

print(answer)
