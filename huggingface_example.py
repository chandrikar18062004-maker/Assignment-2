import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HUGGINGFACE_API_KEY"),
)

try:
    user_input = input("Enter the prompt: ")
    
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[
            {"role": "user", "content": user_input}
        ],
        max_tokens=200
    )
    
    print("HuggingFace:", response.choices[0].message.content)

except Exception as e:
    print("Error:", e)