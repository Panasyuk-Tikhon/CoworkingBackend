from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Solutions

def index(request):
    return HttpResponse("index")

def solutions(request):
    raw_solutions = Solutions.objects.all()
    solutions = []
    print(raw_solutions)
    for solution in raw_solutions.values():
        print(solution)
        solutions.append(solution)
    print(solutions)
    return JsonResponse(solutions, safe=False)

def userPage(request):
    return HttpResponse()

def regLogPage(request):
    return HttpResponse()
