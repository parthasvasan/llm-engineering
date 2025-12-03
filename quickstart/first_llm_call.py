from dotenv import load_dotenv
import os
from openai import OpenAI
import json

# loads environment variables from .env file
load_dotenv()

# gets the API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# checks if the API key is set
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set")

# defines the messages to be sent to the LLM. 
# system message is the instructions for the LLM
# user message is the input to the LLM
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
]

# creates a new OpenAI client
openai = OpenAI()

# sends the messages to the LLM and gets the response
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

# prints the response from the LLM
print(response.choices[0].message.content)