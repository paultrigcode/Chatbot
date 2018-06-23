from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pickle
import os

from datetime import datetime, time

@csrf_exempt
def index(request):
    if request.method == "GET":
        return render(request, 'review/questions.html')
    if request.method == "POST":
        if not os.path.exists('rating_db'):
            data = {
            'q1' :[0, 0, 0, 0],
            'q2' : [0, 0, 0, 0],
            'q3' : [0, 0, 0, 0],
            'q4' : [0, 0, 0, 0],
            'q5' : [0, 0, 0, 0],
            'q6' : [0, 0, 0, 0],
            'q7' : [0, 0, 0, 0]
        }

        else:
            with open('rating_db','rb') as fp:
                data = pickle.load(fp)
        
        new_data = request.POST
        # print('new_data', new_data)
        for _data in new_data:
            val = int(new_data[_data])
            print('val', val)
            if val == 100:
                data[_data][0] += 1
            elif val == 75:
                data[_data][1] += 1
            elif val == 50:
                data[_data][2] += 1
            elif val == 25:
                data[_data][3] += 1
            # print('data[_data]', data[_data])
            # print('new_data[_data]', new_data[_data])
            # data[_data] += new_data[_data]

        with open('rating_db','wb') as fp:
            pickle.dump(data, fp)

        print(data)
        
        # data = {
        #     'q1' :[1, 0, 1, 0],
        #     'q2' : [0, 2, 0, 0],
        #     'q3' : [0, 1, 0, 1],
        #     'q4' : [1, 0, 1, 0],
        #     'q5' : [0, 1, 1, 0],
        #     'q6' : [1, 0, 0, 1],
        #     'q7' : [2, 0, 0, 0]
        # }
        
        data_excellent = []
        data_good = []
        data_average = []
        data_bad = []

        for que in data:
            data_excellent.append(data[que][0])
            data_good.append(data[que][1])
            data_average.append(data[que][2])
            data_bad.append(data[que][3])

        result = {
            'excellent': data_excellent,
            'good': data_good,
            'average': data_average, 
            'bad': data_bad
        }

        print(result)
        
 
        return render(request, 'review/summary.html', {'data': result})
