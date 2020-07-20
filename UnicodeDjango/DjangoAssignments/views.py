from django.shortcuts import render, HttpResponse
from .rangeCheck import checkBits

def index(request):
    return render(request, 'DjangoAssignments/index.html')

def taskTwo(request, start, end):
    return HttpResponse(str(checkBits(start,end)))
# Create your views here.
#, start, end