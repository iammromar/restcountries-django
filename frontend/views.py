from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.


def countries(request):
    data= requests.get("https://restcountries.com/v3.1/all").json()
    return render(request,"index.html",{"con":data,"total":len(data)}) 