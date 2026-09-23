import requests

from .base import LLM


class OllamaClient(LLM):

    def __init__(
        self,
        model="qwen3.5:2b",
        base_url="http://localhost:11434",
    ):
        self.model = model
        self.base_url = base_url

    def generate(self, prompt: str) -> str:

        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            },
        )

        response.raise_for_status()

        data = response.json()

        return data["response"]
