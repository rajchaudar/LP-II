import random

name = "SimpleBot"
mood = "Happy"
weather = "Sunny"

responses = {
    "what's your name?": [
        "My name is {0}".format(name),
        "I am called {0}".format(name),
        "They call me {0}".format(name)
    ],
    "how are you?": [
        "I am feeling {0}".format(mood),
        "I am {0}! How about you?".format(mood),
        "I am {0}! How are you?".format(mood),
    ],
    "what's the weather like?": [
        "The weather is {0}".format(weather),
        "It's a {0} day.".format(weather),
    ],
    "default": [
        "I didn't quite understand that.",
        "Sorry, can you rephrase that?"
    ]
}

def get_response(message):
    return random.choice(responses.get(message.lower(), responses["default"]))

# Chat loop
print(f"{name} is ready to chat! (type 'exit' to stop)")

while True:
    user_input = input("You: ").lower()
    
    if user_input == "exit":
        print(f"{name}: Bye! Have a great day!")
        break
    
    response = get_response(user_input)
    print(f"{name}: {response}")