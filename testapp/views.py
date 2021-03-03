from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def hello(request):
    date=datetime.datetime.now()
    msg='<h1>Hello apurva good morning</h1>'
    msg=msg+'<h1>the server time :'+str(date)+'</h1>'
    return HttpResponse(msg)
