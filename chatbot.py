def chatbot():
    print("🤖 AI Chatbot")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        # Greeting
        if user in ["hi", "hello", "hey"]:
            print("Bot: Hello! How can I help you?")

        # Name
        elif "your name" in user:
            print("Bot: My name is AI Chatbot.")

        # How are you
        elif "how are you" in user:
            print("Bot: I'm doing great! Thanks for asking.")

        # Time
        elif "time" in user:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print("Bot: Current time is", current_time)

        # Date
        elif "date" in user:
            from datetime import datetime
            current_date = datetime.now().strftime("%d-%m-%Y")
            print("Bot: Today's date is", current_date)

        # Weather
        elif "weather" in user:
            print("Bot: I cannot check live weather, but it looks nice today!")

        # Help
        elif "help" in user:
            print("Bot: I can answer greetings, date, time, weather, and more.")

        # AI
        elif "ai" in user:
            print("Bot: AI stands for Artificial Intelligence.")

        # Thanks
        elif "thank" in user:
            print("Bot: You're welcome!")

        # Goodbye
        elif user in ["bye", "goodbye", "exit"]:
            print("Bot: Goodbye! Have a great day.")
            break

        # Favorite color
        elif "favorite color" in user:
            print("Bot: I like blue because it represents technology.")

        # Fallback response (Bonus)
        else:
            print("Bot: Sorry, I don't understand that. Please try another question.")

# Run chatbot
chatbot()
