import openai
import os

client = openai.OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def chat_with_gtp(prompt):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}],
    )
    return response.choices[0].message['content'].strip()

if __name__ == "__main__":
    while True:
        user_input = input("You:")
        if user_input == "exit":
            break
        response = chat_with_gtp(user_input)
        print("Bot:", response)
        