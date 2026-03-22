# from langchain.chat_models import init_chat_model
# from langchain_core.messages import HumanMessage
# import base64
# import requests

# # Use Llama 3.2 Vision (3.1 doesn't support images)
# model = init_chat_model("llama3.2-vision", model_provider="ollama")

# # Download and encode the image as base64
# image_url = "https://www.freepik.com/premium-photo/bird-photorealistic-red-billed-toucan-blue-yellow-macaw_32298256.htm#from"
# response = requests.get(image_url)
# base64_image = base64.b64encode(response.content).decode('utf-8')

# # Create message with base64 image
# message = HumanMessage(
#     content=[
#         {"type": "text", "text": "Describe the content of this image."},
#         {
#             "type": "image_url",
#             "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
#         }
#     ]
# )

# response = model.invoke([message])
# print(response.content)

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
import base64
import requests

model = init_chat_model("llama3.2-vision", model_provider="ollama")

# Use a DIRECT image URL (not a webpage)
image_url = "https://images.unsplash.com/photo-1552728089-57bdde30beb3?w=800"  # Toucan image

response = requests.get(image_url)
base64_image = base64.b64encode(response.content).decode('utf-8')

message = HumanMessage(
    content=[
        {"type": "text", "text": "Describe the content of this image."},
        {
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
        }
    ]
)

response = model.invoke([message])
print(response.content)