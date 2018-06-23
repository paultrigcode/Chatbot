from . ydialogue import YorubaDialogue

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chat.dialogue.story import TRAINING_DATA, FLOW
from chat.dialogue import Dialogue

def save_to_db(sentence):
    with open('db', 'w') as fp:
        fp.write()

def load_response(sentence):
    # direct lookup
    d = Dialogue()
    tagged_response = d.parse_sentence(sentence)
    # print("direct look up response:", response)
    # print("substitutions:", d.substitutions)
    response = d.refill_tags(tagged_response)
    print('direct substitution response:', response)
    

    # old shitty lookup
    if not response:
        dailogue = YorubaDialogue()
        response = dailogue.respond(sentence)
        print("old shitty response", response)
    
    # chat bot lookup
    try:
        if not response:
            chatbot = load_chatbot()
            response = get_bot_response(sentence, chatbot)
            print("bot response", response)
    except:
        response ="Ẹ sàlàyé síwájú si"
    
    return str(response).capitalize()


def load_chatbot():
    with open('ajantala/chat/dialogue.txt', 'r') as fp:
        conversation = fp.readlines()

    chatbot = ChatBot("Ajantala")
    chatbot.set_trainer(ListTrainer)
    chatbot.train(TRAINING_DATA)

    return chatbot

def get_bot_response(sentence, bot):
    response = bot.get_response(sentence)
    print("respnose confidence: ", response.confidence)
    if response.confidence < 0.5:
        return  "Ẹ sàlàyé síwájú si"
    return response
