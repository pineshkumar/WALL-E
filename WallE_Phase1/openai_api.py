import openai
import config  # Import API key from config.py

openai.api_key = config.OPENAI_API_KEY

def interpret_command(command):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"What does '{command}' mean in terms of motor control?"}]
    )
    return response["choices"][0]["message"]["content"].lower()
