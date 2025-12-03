from dotenv import load_dotenv
import os
from openai import OpenAI
import json
from PyPDF2 import PdfReader
from IPython.display import Markdown, display

# loads environment variables from .env file
load_dotenv()

# gets the API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# checks if the API key is set
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set")

# Extracts text from a pdf document
def extract_text_from_document(document_path):
    """
    Extracts content from the document at the given path and returns it as a string.
    """
    reader = PdfReader(document_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Calls the LLM with the given messages and returns the response
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
    Main function to summarize the document at the given path.
    """
    document_path = "data/document.pdf"
    content = extract_text_from_document(document_path)
    #print(content)

    messages = [
        {"role": "system", "content": "You are a helpful assistant that can read, analyze content of a document and come up with an appropriate title for the document."},
        {"role": "user", "content": "Provide analyze the content of the following document and come up with an appropriate title for the document: " + content + " The title should be a single sentence, crisp, concise, and should be no more than 10 words."}
    ]
    response = call_llm(messages)
    print(response)
    

if __name__ == "__main__":
    main()