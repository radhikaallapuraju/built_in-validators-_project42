from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse

# Create your views here.

def insert_topic(request):
    TF=TopicForm()
    d={'TF':TF}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
        else:
            return HttpResponse('date is not valid')
    return render(request,'insert_topic.html',d)
