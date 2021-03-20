from django.shortcuts import render
from .models import Inputs
from django.http import HttpResponse

def add(request):
    if request.method=="POST":
        inputs=Inputs()
        fname=request.POST.get('fname')  
        lname=request.POST.get('lname')
        inputs.fname=fname
        inputs.lname=lname
        inputs.save()
        return HttpResponse("<h1>Name Submitted</h1>")
    return render(request, 'store/add.html')


def home(request):
    context = {}
    return render(request, 'store/home.html')


def forms(request):
    context = {}
    return render(request, 'store/forms.html')


