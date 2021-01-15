from chatterbot import ChatBot
from chatterbot.trainers import UbuntuCorpusTrainer

chatbot = ChatBot('Ron Obvious')
trainer = UbuntuCorpusTrainer(chatbot)
trainer.train()


