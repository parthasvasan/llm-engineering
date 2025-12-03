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
    Summarizes the document at the given path.
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
        {"role": "system", "content": "You are a helpful assistant that can read and summarize large documents. You are given a document and you need to summarize it in a few sentences."},
        {"role": "user", "content": "Provide an executive summary of the following document: " + content + " DOn not include mark down formatting."}
    ]
    response = call_llm(messages)
    print(response)
    

if __name__ == "__main__":
    main()