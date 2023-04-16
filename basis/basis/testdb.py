from django.http import HttpResponse
from django.db import connection 
from basisModel.models import *

def testdb(request):
    list = Car.objects.all()
    response = ""
    for var in list:
        response += var.name + " "
    # with connection.cursor() as cur:
    #     cur.execute("select name from car")
    # str = cur.fetchall()
    # str = Car.objects.all().name
    return HttpResponse("<p>"+response+"</p>")