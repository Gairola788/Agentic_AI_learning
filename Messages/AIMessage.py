from langchain.messages import AIMessage,SystemMessage,HumanMessage
from langchain.chat_models import init_chat_model

model = init_chat_model("llama3.2", model_provider="ollama")

#creating an AI message manually -> for conversation history 
ai_msg = AIMessage("I'd be happy to help you with that question!")

#Add to  conversation history

# messages = [
#     SystemMessage("You are a helpful assistant"),
#     HumanMessage("Can you help me? "),
#     ai_msg, #Insert as if  it came from the model
#     HumanMessage("Great! What's the factorial of 5")
# ]

# response = model.invoke("Hello!")
# # print(response.text)
# # print(response.tool_calls)
# print(response.usage_metadata)

chunks = []
full_message = None
for chunk in model.stream("Hi"):
    chunks.append(chunk)
    print(chunk.text)
    full_message = chunk if full_message is None else full_message + chunk