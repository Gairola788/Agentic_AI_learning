#Messages are the fundamental unit of context for models in Langchain.
# They represent the input and output of models, carrying both the content and metadata needed to represent the state of a conversation when interacting with an LLM.

from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage,SystemMessage

model = init_chat_model("llama3.2", model_provider="ollama")

# system_msg = SystemMessage("You are a helpful assistant.")
# human_msg = HumanMessage("Hello,how are you?")

# #Use with chat models
# messages = [system_msg,human_msg]
# response = model.invoke(messages)
# print(response.content)

#Message prompts
# messages = [
#     SystemMessage("You are a Story teller"),
#     HumanMessage("Explain the story of world war 2 "),
#     AIMessage("USA emerged as the supreme Leader after world war 2")
# ]

# response = model.invoke(messages)

# messages = [
#     {"role": "system", "content": "You are a poetry expert"},
#     {"role": "user", "content": "Write a haiku about spring"},
#     {"role": "assistant", "content": "Cherry blossoms bloom..."}
# ]
# response = model.invoke(messages)

# print(response.content)


# SystemMessage
system_msg = SystemMessage("""You are a senior Python developer with expertise in web frameworks.
Always provide code examples and explain your reasoning.
Be concise but thorough in your explanations.""")

messages = [
         system_msg,
         HumanMessage("Give the code for factorial of a number using python")
]

# response = model.invoke(messages)
# print(response.content)

# human_msg = HumanMessage(
#     content="Hello!",
#     name="alice",  # Optional: identify different users
#     id="msg_123",  # Optional: unique identifier for tracing
# )

# response = model.invoke(human_msg)
# print(response.content)

response = model.invoke("Explain AI")
print(type(response))  # <class 'langchain.messages.AIMessage'>
