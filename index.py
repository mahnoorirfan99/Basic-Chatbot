import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help?"],
    "how are you": ["I'm just a bot, but I'm doing great! How about you?", "Feeling chatty today!"],
    "what is your name": ["I'm a chatbot!", "Just call me ChatBot."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    return "Sorry I didn't get it"

print("Chatbot: Hi!, Type 'bye' to exit")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("ChatBot:", random.choice(responses["bye"]))
        break
    print("ChatBot:", chatbot_response(user_input))