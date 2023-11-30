from django.shortcuts import render

def home(request):
    return render(request, 'home.html');

def show_item(request):
    return render(request, 'show_item.html');