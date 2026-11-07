from pydantic_ai import Agent
from pydantic import BaseModel
from dataclasses import dataclass
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from dotenv import load_dotenv
import os

from tools.log import show_logs


load_dotenv()

tools = [show_logs]

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("Found api key!")

provider = GoogleProvider(api_key=GEMINI_API_KEY)
model = GoogleModel('gemini-3.5-flash-lite', provider=provider)


response_agent = Agent(
    model=model,
    instructions="You are a desktop AI assistant. Your job is to serve the user and use tools when needed.",
    tools=tools
)


