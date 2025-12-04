from dotenv import load_dotenv
import os
from openai import OpenAI
import json
import requests
# loads environment variables from .env file
load_dotenv()

# gets the API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# checks if the API key is set
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set")

def call_api_endpoint(endpoint, data):
    """
    Calls the given API endpoint with the given data and returns the response.
    """
    url = f"https://api.openai.com/v1/{endpoint}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

def main():
    """
    Main function to call the API endpoint with the given data.
    """
    endpoint = "chat/completions"
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": "Tell me a fun fact about prime numbers."}]
    }
    print(json.dumps(call_api_endpoint(endpoint, data), indent=4))
    print("--------------------------------")
    print("Response:")
    print(call_api_endpoint(endpoint, data)["choices"][0]["message"]["content"])

if __name__ == "__main__":
    main()