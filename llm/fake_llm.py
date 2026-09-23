from .base import LLM


class FakeLLM(LLM):

    def generate(self, prompt: str) -> str:
        return (
            "This is a test response from the FakeLLM. "
            "The RAG pipeline successfully generated a prompt."
        )
