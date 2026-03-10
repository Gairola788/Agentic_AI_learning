##Tool calling
'''Models can request to call tools that perform tasks such as fetching data from a database, searching the web, or running code. Tools are pairings of:
1 -> A schema, including the name of the tool, a description, and/or argument definitions (often a JSON schema)
2 -> A function or coroutine to execute.'''


from langchain.chat_models import init_chat_model
from langchain.tools import tool

model = init_chat_model("llama3.1", model_provider="ollama")

@tool 
def get_weather(location: str) -> str:
    """Get the weather at a location."""
    return f"It's sunny in {location}."

model_with_tools = model.bind_tools([get_weather])

# response = model_with_tools.invoke("What's the weather like  in Botson?")
# for tool_call in response.tool_calls:
#     # View tool calls made by the model
#     print(f"Tool: {tool_call['name']}")
#     print(f"Args: {tool_call['args']}")
    
# print(response.content)

#  Step 1: Model generates tool calls
messages = [{"role": "user", "content": "What's the weather in Boston?"}]
ai_msg = model_with_tools.invoke(messages)
messages.append(ai_msg)

# Step 2: Execute tools and collect results
for tool_call in ai_msg.tool_calls:
    # Execute the tool with the generated arguments
    tool_result = get_weather.invoke(tool_call)
    messages.append(tool_result)

# Step 3: Pass results back to model for final response
final_response = model_with_tools.invoke(messages)
print(final_response.text)
# "The current weather in Boston is 72°F and sunny."

