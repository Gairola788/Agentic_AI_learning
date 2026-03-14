from langchain.chat_models import init_chat_model

model = init_chat_model("llama3.1", model_provider="ollama")

response = model.invoke("Create a picture of a cat")
print(response.content_blocks)

# Reasoning of Models
# Many models are capable of performing multi-step reasoning to arrive at a conclusion. 
# This involves breaking down complex problems into smaller, more manageable steps.

for chunk in model.stream("Why do parrots have colorful feathers?"):
    reasoning_steps = [r for r in chunk.content_blocks if r["type"] == "reasoning"]
    print(reasoning_steps if reasoning_steps else chunk.text)