from prompt_builder import PromptBuilder


question = "Have we seen unusual temperature increases before?"

context = """
Sensor S01 experienced an unusual temperature increase
from 22 degrees Celsius to 31 degrees Celsius over two hours.

Sensor S02 showed stable temperature readings around
24 degrees Celsius.
"""

builder = PromptBuilder()

prompt = builder.build(question, context)

print(prompt)
