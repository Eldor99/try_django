from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request,'home.html', {'title': "Home page"})

def about_page(request):
    return render(request,'about.html', {'title': "About Us"})

def contact_page(request):
    return render(request,'hello_world.html', {'title': "Contact US"})