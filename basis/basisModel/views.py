from django.shortcuts import render

# Create your views here.
from models import *

names = [i for i in dir(Build) if i not in dir(Base)]
print(names)