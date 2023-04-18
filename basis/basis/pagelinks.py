from django.http import HttpResponse
from django.shortcuts import render
from . import testdb
from basisModel.models import * 
from basisModel.views import *
import json
# 表单
def search_form(request):
    # username = request.GET['user']
    return render(request, 'search_form.html',{'user':'test','message':"hello world"})

def child(request):
    return render(request,'child.html',{'message':"hello"})

def search_post(request):
    ctx = {}
    if request.POST:
        ctx['name'] = request.POST['name']
        ctx['message'] = getcust(ctx['name'])
    return render(request,"child.html",{'ctx':ctx})