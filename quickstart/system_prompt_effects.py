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

def call_llm(messages):
    """
    Calls the LLM with the given messages and returns the response.
    """
    openai = OpenAI()
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return response.choices[0].message.content
    
def main():    
    """
    Main function to call the LLM with the given messages. Demonstrates the effects of the 
    system prompt on the LLM's response. The LLM's response is printed to the console.
    """
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
    print(call_llm(messages))

    messages = [
        {"role": "system", "content": "You are a snarky assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
    print(call_llm(messages))

    messages = [
        {"role": "system", "content": "You are a grumpy assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
    print(call_llm(messages))

if __name__ == "__main__":
    main()