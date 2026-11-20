from chatbot import ChatBot

bot = ChatBot()

print("AI Chatbot Started!")
print("Type 'exit' to stop the conversation.")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Chatbot stopped.")
        break

    try:

        response = bot.get_response(user_input)

        print("\nAI:", response)

    except Exception as e:

        print("Error:", e)