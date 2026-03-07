import os
from langchain.chat_models import init_chat_model

model = init_chat_model("llama3.1", model_provider="ollama")
response = model.invoke("Why do parrots talk?")  # correct comment syntax
print(response.content)