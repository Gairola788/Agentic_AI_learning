import os
from langchain.chat_models import init_chat_model


# model = init_chat_model("llama3.1", model_provider="ollama")

model = init_chat_model(
    "ollama:llama3.1",
    # Kwargs passed to the model:
    temperature=0.7,
    timeout=30,
    max_tokens=1000,
    max_retries=6,  # Default; increase for unreliable networks
)
response = model.invoke("Why do parrots talk?")  # correct comment syntax
print(response.content)