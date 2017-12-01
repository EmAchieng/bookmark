from django.shortcuts import render
from django.http import HttpResponse

import datetime
# Create your views here.

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body> It is now %s. </body></html>" %now
    return HttpResponse(html)

def new_time(request):
    now = datetime.datetime.now()
    return render(request, "hello.html", {"now": now})

def hello(request, user_name):
    html = "<html><body> Hello. %s </body></html>" % user_name
    return HttpResponse(html)