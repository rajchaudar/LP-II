from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

chatbot = ChatBot('SimpleBot')

trainer = ChatterBotCorpusTrainer(chatbot)

# Train with default and custom corpus
trainer.train('chatterbot.corpus.english')  # Optional
trainer.train('/Users/Shivrajchaudar/myenv/lib/python3.9/site-packages/chatterbot_corpus/data/english') 

print("SimpleBot is ready to chat! (type 'exit' to stop)")
while True:
    user_input = input("You: ").lower()
    if user_input == "exit":
        print("SimpleBot: Bye! Have a great day!")
        break
    response = chatbot.get_response(user_input)
    print(f"SimpleBot: {response}")