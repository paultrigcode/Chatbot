from . ydialogue import YorubaDialogue

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def save_to_db(sentence):
    with open('db', 'w') as fp:
        fp.write()

def load_response(sentence):
    dailogue = YorubaDialogue()
    respond = dailogue.respond(sentence)
    print("respond", respond)
    chatbot = load_chatbot()
    # bot_response = chatbot.get_response(sentence)
    bot_response = "kò yé mi"
    print("bot response", bot_response)
    return respond if respond else bot_response 


def load_chatbot():
    with open('chat/dialogue.txt', 'r') as fp:
        conversation = fp.readlines()

    chatbot = ChatBot("Ajantala")
    chatbot.set_trainer(ListTrainer)
    chatbot.train(conversation)

    return chatbot