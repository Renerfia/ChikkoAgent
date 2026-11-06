from pydantic_ai import Agent
from pydantic import BaseModel
from dataclasses import dataclass
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from dotenv import load_dotenv
import os 

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("Found api key!")

provider = GoogleProvider(api_key=GEMINI_API_KEY)
model = GoogleModel('gemini-3.6-flash', provider=provider)


response_agent = Agent(
    model=model,
    instructions="You are a desktop AI assistant. Your job is to server the user and use the tool if needed."
    
)