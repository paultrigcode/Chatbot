from . ydialogue import YorubaDialogue

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chat.dialogue.story import FLOW

def save_to_db(sentence):
    with open('db', 'w') as fp:
        fp.write()

def load_response(sentence):
    dailogue = YorubaDialogue()
    response = dailogue.respond(sentence)
    print("response", response)
    chatbot = load_chatbot()
    bot_response = get_bot_response(sentence, chatbot)
    print("bot response", bot_response)
    return response if response else bot_response 


def load_chatbot():
    with open('chat/dialogue.txt', 'r') as fp:
        conversation = fp.readlines()

    chatbot = ChatBot("Ajantala")
    chatbot.set_trainer(ListTrainer)
    chatbot.train(FLOW)

    return chatbot

def get_bot_response(sentence, bot):
    response = bot.get_response(sentence)
    print("respnose confidence: ", response.confidence)
    if response.confidence < 0.5:
        return  "Ẹ sàlàyé síwájú si"
    return response
