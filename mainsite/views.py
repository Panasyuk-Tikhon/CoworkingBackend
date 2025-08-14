from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Solutions
# Create your views here.

def index(request):
    solutions = Solutions.objects.all()
    print(solutions)
    for solution in solutions:
        print(solution)
    return HttpResponse("work")
    #return JsonResponse(solutions, safe=False)

def userPage():
    return HttpResponse()

def regLogPage():
    return HttpResponse()
