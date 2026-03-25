import os
import cohere
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

try:
    user_input = input("Enter the prompt: ")
    response = co.chat(message=user_input)
    print("Cohere:", response.text)
except Exception as e:
    print("Error:", e)