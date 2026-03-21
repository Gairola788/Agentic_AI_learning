from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage


model = init_chat_model("llama3.1", model_provider="ollama")

#String  content
# human_message = HumanMessage("Hello, how are you?")

#List of standard content blocks
human_message = HumanMessage(
    content=[
        {"type": "text", "text": "Hello, how are you?"},
        {
            "type": "image_url",
            "image_url": {
                "url": "C:\Users\Gairo\OneDrive\Desktop\carss.jpg"  # Or use data:image/jpeg;base64,...
            }
        }
    ]
)

response = model.invoke([human_message])
print(response.text)

