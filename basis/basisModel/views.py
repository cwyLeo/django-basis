from django.shortcuts import render

# Create your views here.
from basisModel.models import *

def getcust(name):
    cust = Customer.objects.get(name=name)
    return cust