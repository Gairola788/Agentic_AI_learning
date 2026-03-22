"""Tools extend what agents can do—letting them fetch real-time data, execute code, query external databases, and take actions in the world.
Under the hood, tools are callable functions with well-defined inputs and outputs that get passed to a chat model. 
The model decides when to invoke a tool based on the conversation context, and what input arguments to provide.
"""

from langchain.chat_models import init_chat_model

model = init_chat_model("llama3.2-vision", model_provider="ollama")

