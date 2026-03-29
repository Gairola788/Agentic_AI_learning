"""Tools extend what agents can do—letting them fetch real-time data, execute code, query external databases, and take actions in the world.
Under the hood, tools are callable functions with well-defined inputs and outputs that get passed to a chat model. 
The model decides when to invoke a tool based on the conversation context, and what input arguments to provide.
"""

from langchain.chat_models import init_chat_model
from langchain.tools import tool


model = init_chat_model("llama3.2-vision", model_provider="ollama")


@tool
def search_database(query: str,limit:int = 10) -> str:
    """Search the customer database for records matching the query.

    Args:
        query: Search terms to look for
        limit: Maximum number of results to return
    """
    return f"Found {limit} results for '{query}'"

#Customize tool properties
#Custom tool name

"""By default, the tool name comes from the function name. 
Override it when you need something more descriptive:"""

@tool("web_search")  #Custom name
def search(query: str) -> str:
    """Search the web for information."""
    return f"Results for: {query}"

print(search.name) # web_search

#Custom tool Description
@tool("calculator",description="Performs arithmetic Calculations.Use this for any Math Problems.")
def calc(expression:str) -> str:
    """Evaluate mathematical expressions."""
    return str(eval(expression))






