from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from . utils import load_response, save_to_db

import pickle
from datetime import datetime, time

@csrf_exempt
def index(request):
    if request.method == "POST":
        sentence = request.POST.get('sentence')
        #print("sentence", sentence)
        text_response = load_response(sentence)
        # load existing convos ..
        with open('db','rb') as fp:
            conversations = pickle.load(fp)
        
        # add current convo to exisiting convo
        time = datetime.now().strftime('%H:%M')
        conversations.append({'sentence': sentence, 'reply': text_response, 'time': time})

        # update convo db
        with open('db','wb') as fp:
            pickle.dump(conversations, fp)
        
        print('conversations', conversations)

        greeting = load_greetings()
        return render(request, 'chat/result.html', {'conversations': conversations, 'greeting': greeting})
    
    elif request.method == "GET":
        conversations = []
        # clear db
        with open('db','wb') as fp:
            conversations = pickle.dump(conversations, fp)
        greeting = load_greetings()
        return render(request, 'chat/index.html', {"greeting": greeting})


def load_greetings():
    now = datetime.now()
    now_time = now.time()
    if now_time <= time(4, 00):
        return "Ẹ káàbọ̀, Ẹ káalẹ́!!!"
    elif now_time <= time(6, 00):
        return "Ẹ káàbọ̀, Ẹ kú ìdájí!!!"
    elif now_time <= time(10, 00):
        return "Ẹ káàbọ̀, Ẹ káàárọ̀!!!"
    elif now_time < time(12, 00):
        return "Ẹ káàbọ̀, Ẹ kú ìyálẹ́ta!!!"
    elif now_time <= time(13, 00):
        return "Ẹ káàbọ̀, E ku ojokanri!!!"
    elif now_time <= time(15, 00):
        return "Ẹ káàbọ̀, Ẹ  káàsán!!!"
    elif now_time <= time(19, 00):
        return "Ẹ káàbọ̀, Ẹ kúrọ̀lẹ́!!!"
    elif now_time <= time(23, 59):
        return "Ẹ káàbọ̀, Ẹ káalẹ́!!!"