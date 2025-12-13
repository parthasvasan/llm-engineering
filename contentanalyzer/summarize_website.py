from re import T
from bs4 import BeautifulSoup
import requests
from openai import OpenAI
from IPython.display import Markdown, display
from dotenv import load_dotenv
import os

def load_environment_variables():
    """
    Loads the environment variables from the .env file.
    """
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set")
    return api_key

def get_website_content(url):
    """
    Gets the content of the website at the given URL.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else "No title found."
    if soup.body:
        for items in soup.body.find_all(["script", "style", "img", "input"]):
            items.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""
    
    return (title + "\n\n" + text)[:2000] if len(title + "\n\n" + text) > 2000 else (title + "\n\n" + text)

def get_system_prompt():
    """
    Gets the system prompt for the website summarizer.
    """
    system_prompt = """
You are a helpful assistant that analyzes the contents of a website,
and provides a short, concise summary, ignoring text that might be navigation related.
Respond in well formatted plain text.
"""
    return system_prompt

def get_user_prompt(content):
    """
    Gets the user prompt for the website summarizer.
    """
    user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.

"""
    return user_prompt_prefix + content

def get_messages(content):
    """
    Gets the messages for the website summarizer.
    """
    messages = [
        {"role": "system", "content": get_system_prompt()},
        {"role": "user", "content": get_user_prompt(content)}
    ]
    return messages

def summarize_website(url):
    """
    Summarizes the website at the given URL.
    """
    content = get_website_content(url)
    messages = get_messages(content)
    response = call_llm(messages)
    return response

def call_llm(messages):
    """
    Calls the LLM with the given messages and returns the response.
    """
    openai = OpenAI()
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages)
    return response.choices[0].message.content

def main():
    """
    Main function to get the content of the website at the given URL.
    """
    load_environment_variables()
    url = "https://linkedin.com"
    content = get_website_content(url)
    summary = summarize_website(url)
    print(summary)
    

if __name__ == "__main__":
    main()