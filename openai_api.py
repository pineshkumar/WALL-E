import openai
import config  # Import API key from config.py

openai.api_key = config.OPENAI_API_KEY  # Store your API key in config.py

def process_command(command):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": command}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    user_input = "Move forward"
    print(process_command(user_input))
