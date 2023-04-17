from django.http import HttpResponse
from django.shortcuts import render
from . import testdb
from basisModel.models import * 
import json
# 表单
def search_form(request):
    # username = request.GET['user']
    return render(request, 'search_form.html',{'user':'test','message':"hello world"})