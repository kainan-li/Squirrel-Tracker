from django.shortcuts import render
from squirrel.models import squirrel
from django.http import HttpResponse
from .forms import SquirrelForm
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




def editsightings(request,squirrel_id):

    queryset = squirrel.objects.filter(unique_squirrel_id=squirrel_id)
    if request.POST:
        form=squirrel(request.POST,instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('sightings')
    

def stats(request):
    squirrels=squirrel.objects.all()
    context={
              's':squirrels
            }
    return render(request,'squirrel/stats.html',context)


def add(request):
    if request.method == 'POST':
        #check form data
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'sightings/')
    else:
        form = SquirrelForm()
    context = {
        'form':form,
    }
    return render(request, 'squirrel/add.html',context)

