from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from datetime import datetime, time

@csrf_exempt
def index(request):
    
    if request.method == "GET":
        return render(request, 'review/questions.html')
