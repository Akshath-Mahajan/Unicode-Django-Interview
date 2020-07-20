from django.shortcuts import render, HttpResponse
from .rangeCheck import checkBits
import requests
from .models import Weather
from django.db.models import F
from datetime import date

def storeApiData(data): #Helper function for storing data
    city = data['name']
    country = data['sys']['country']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    weather = data['weather'][0]['main']
    description = data['weather'][0]['description']
    temperature = data['main']['temp']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    visibility = data['visibility']
    wind_speed = data['wind']['speed']
    weather = Weather(city=city, country=country, latitude=latitude, longitude=longitude, weather=weather, description=description, temperature=temperature, pressure=pressure, humidity=humidity, visibility=visibility, wind_speed=wind_speed)
    weather.save()

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
        #Storing the response in db for task 4A below:
        data = eval(response.text)
        if data['cod'] != '404':
            storeApiData(data)
        return render(request, 'DjangoAssignments/taskThree.html', {'response':response.text})

def taskFourA(request):
    if request.method == "GET":
        return render(request, 'DjangoAssignments/taskFourA.html')
    if request.method == "POST":
        date = request.POST['date'].split('-')
        city = request.POST['city']
        data = Weather.objects.filter(city=city).filter(date__year=date[0], 
                                                date__month=date[1], 
                                                date__day=date[2])
        data.update(count=F('count') + 1)
        return render(request, 'DjangoAssignments/taskFourA.html', {'response':data})

def taskFourB(request):
    data = Weather.objects.all().order_by('-count')[:3]
    return render(request, 'DjangoAssignments/taskFourB.html', {'response':data})

