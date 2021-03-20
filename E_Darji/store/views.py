from django.shortcuts import render


def add(request):
    context = {}
    return render(request, 'store/add.html', context)


def home(request):
    context = {}
    return render(request, 'store/home.html', context)




