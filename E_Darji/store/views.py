from django.shortcuts import render
from store.models import Inputs, Forms
from django.http import HttpResponse
from django.contrib import messages

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
    return render(request, 'store/home.html')


def forms(request):
    if request.method == "POST":
        Name = request.POST.get('name')
        Contact = request.POST.get('Contact')
        Length = request.POST.get('Length')
        Shoulder = request.POST.get('Shoulder')
        Chest = request.POST.get('Chest')
        Sleeves = request.POST.get('Sleeves')
        Neck = request.POST.get('Neck')
        Arm = request.POST.get('Arm')
        Width = request.POST.get('Width')
        Sleevehole = request.POST.get('Sleevehole')
        Hip = request.POST.get('Hip')
        Breast = request.POST.get('Breast')
        Quantity = request.POST.get('Quantity')
        Lengthp = request.POST.get('Lengthp')
        Hipp = request.POST.get('Hipp')
        Waist = request.POST.get('Waist')
        Bottom = request.POST.get('Bottom')
        Knees = request.POST.get('Knees')
        Calf = request.POST.get('Calf')
        quantity = request.POST.get('quantity')
        extra = request.POST.get('extra')     

        forms = Forms(Name=Name, Contact=Contact, Length=Length, Shoulder=Shoulder, Chest=Chest, Sleeves=Sleeves, 
                      Neck=Neck, Arm=Arm, Width=Width, Sleevehole=Sleevehole, Hip=Hip, Breast=Breast, 
                      Quantity=Quantity, Lengthp=Lengthp, Hipp=Hipp, Waist=Waist, Bottom=Bottom, Knees=Knees, 
                      Calf=Calf, quantity=quantity, extra=extra)
        forms.save()
        messages.success(request, 'Details updated sucesefully.')
    return render(request, 'store/forms.html')

def summary(request):
    context = {}
    return render(request, 'store/summary.html')
