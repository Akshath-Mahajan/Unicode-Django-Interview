from django.shortcuts import render, HttpResponse
from .rangeCheck import checkBits
import requests

def index(request):
    return render(request, 'DjangoAssignments/index.html')

def taskTwo(request, start, end):
    return HttpResponse(str(checkBits(start,end)))

def taskThree(request):
    if request.method=="GET":
        return render(request, 'DjangoAssignments/taskThree.html')
    if request.method=="POST":
        url = "https://community-open-weather-map.p.rapidapi.com/weather"

        querystring = {"units":"%22metric%22 or %22imperial%22","mode":"xml%2C html","q": request.POST['city']+", "+request.POST['country']}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "a8e6750b45msh1789476a19ccd55p10933djsnef1f0bd7f06e"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return render(request, 'DjangoAssignments/taskThree.html', {'response':response.text})
# Create your views here.
#, start, end