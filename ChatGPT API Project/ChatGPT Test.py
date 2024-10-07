from openai import OpenAI

client = OpenAI(api_key = open("api_key.txt","r").read())

print("ChatGPT 4\n---------")

user_input = input("\nUser: ")

while user_input.lower() != "exit":

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": user_input,}],
        model="gpt-4o-mini",
    )

    print("\nChatGPT: " + chat_completion.choices[0].message.content)

    user_input = input("\nUser: ")