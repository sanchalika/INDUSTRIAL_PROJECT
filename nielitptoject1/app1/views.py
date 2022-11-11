from django.shortcuts import render
from django.http import HttpResponse
import datetime
def g1(request):
    now=datetime.datetime.now()
    html="Time is {}".format(now)

    return HttpResponse(html)

