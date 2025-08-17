# Task 8: Rule-Based Chatbot

print("🤖 Chatbot: Hello! I'm your friendly chatbot. Type 'bye' anytime to quit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("🤖 Chatbot: Hey there! How can I assist you today?")
    elif "how are you" in user_input:
        print("🤖 Chatbot: I'm just code, but I'm feeling awesome! How about you?")
    elif "your name" in user_input:
        print("🤖 Chatbot: My name is RuleBot, a simple chatbot made with Python.")
    elif "help" in user_input:
        print("🤖 Chatbot: You can ask me about my name, greet me, or ask how I am.")
    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        print("🤖 Chatbot: Goodbye! It was nice chatting with you. 👋")
        break
    else:
        print("🤖 Chatbot: Hmm... I don't know how to respond to that yet.")
