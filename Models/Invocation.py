from langchain.chat_models import init_chat_model

model = init_chat_model("llama3.1", model_provider="ollama")

#A chat model must n=be invokked to generate an ouput...

#Invoke->
# The most straightforward way to call a model is to use invoke() with a single message
# or a list of messages.
# response = model.invoke("Why do LLM models hallucinate?")
# print(response)

#List of messages
conversation = [ #Dictionary format
    {"role": "system", "content": "You are a helpful assistant that translates English to French."},
    {"role": "user", "content": "Translate: I love programming."},
    {"role": "assistant", "content": "J'adore la programmation."},
    {"role": "user", "content": "Translate: I love building applications."}
]

response = model.invoke(conversation)
print(response.content)

from langchain.messages import HumanMessage, AIMessage, SystemMessage

conversation = [
    SystemMessage("You are a helpful assistant that translates English to French."),
    HumanMessage("Translate: I love programming."),
    AIMessage("J'adore la programmation."),
    HumanMessage("Translate: I love building applications.")
]

response = model.invoke(conversation)
print(response)  # AIMessage("J'adore créer des applications.")