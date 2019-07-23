from django.shortcuts import render
from django.http import HttpResponse
from static.lists import *

# Create your views here.

def home(request):
    return HttpResponse('<H1>Hello </H1>')

def adnow(request):
    return render(request,'adnow.html',{'CountryList':CountryList,'SlList':SlList,'PlatformVal':PlatformVal,'Methodology':Methodology,'CategoryInForm':CategoryInForm,'ClientList':ClientList,'CategoryInDB':CategoryInDB})
