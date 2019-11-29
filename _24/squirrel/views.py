from django.shortcuts import render
from squirrel.models import squirrel
from django.http import HttpResponse
def map(request):
    data=squirrel.objects.all()
    stu={
            "s":data
    }

    return render(request,'squirrel/map.html',stu)
def sightings(request):
    data=squirrel.objects.all()
    stu={
            "s":data
    }
    return render(request,'squirrel/sightings.html',stu)
