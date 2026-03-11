from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field

model = init_chat_model("llama3.1", model_provider="ollama")

class Movie(BaseModel):
    """Introduction of a Cricketer"""
    title: str = Field(..., description="The title given for the cricketer")
    year: int = Field(..., description="His first Debut date in international cricket")
    Movie: str = Field(..., description="His biography or any movie")
    Records: float = Field(..., description="Total 100's and 50's by him")
    
model_with_structure = model.with_structured_output(Movie)
response = model_with_structure.invoke("Give an introduction about Mahenfra singh Dhoni")
print(response)