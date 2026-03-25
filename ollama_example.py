import requests

try:
    user_input = input("Enter the prompt: ")
    
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": user_input,
            "stream": False
        }
    )
    
    if response.status_code == 200:
        print("Ollama:", response.json()["response"])
    else:
        print("Error:", response.status_code, response.text)

except Exception as e:
    print("Error:", e)