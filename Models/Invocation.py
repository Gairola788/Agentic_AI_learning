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

# response = model.invoke(conversation)
# print(response.content)

from langchain.messages import HumanMessage, AIMessage, SystemMessage

conversation = [
    SystemMessage("You are a helpful assistant that translates English to French."),
    HumanMessage("Translate: I love programming."),
    AIMessage("J'adore la programmation."),
    HumanMessage("Translate: I love building applications.")
]

# response = model.invoke(conversation)
# print(response)  # AIMessage("J'adore créer des applications.")

##Stream-> Most models can stream their output content while it is being generated. 
# By displaying output progressively, streaming significantly improves user experience, 
# particularly for longer responses.

# for  chunk in model.stream("Why do LLM models hallucinate?"):
#     print(chunk.text, end="|",flush=False)
    
##Constructing ans AI message 
# full = None
# for chunk in model.stream("What color is the sky?"):
#     full = chunk if full is None else  full + chunk
#     print(full.text)
    
#print(full.content_blocks)
# [{"type": "text", "text": "The sky is typically blue..."}]


#Batch->
"""Batching a collection of independent requests to a model can significantly improve performance and, 
reduce costs, as the processing can be done in parallel:"""

responses  = model.batch([
    "What are dangerous Inventions in AI",
    "Prdeictions Of AI in 2050?",
    "What is Agentic AI?"
])
for response in responses:
    print(response)


    