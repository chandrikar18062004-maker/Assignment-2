from dotenv import load_dotenv
import os
from google import genai


load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


prompt = input("Enter your prompt: ")


response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt
)


print("\nResponse:")
print(response.text)