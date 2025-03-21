import requests
import config  # Import API key from config.py

def interpret_command(command):
    url = "https://api.openai.com/v1/chat/completions"  # External API URL
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config.OPENAI_API_KEY}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"What does '{command}' mean in terms of motor control?"}]
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"].lower()
    else:
        print("Error:", response.status_code, response.text)
        return ""
