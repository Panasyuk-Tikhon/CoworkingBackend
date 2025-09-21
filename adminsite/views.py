from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello admin")

def getOrders(request):
    return HttpResponse("gotten")

def acceptOrder(request):
    return HttpResponse("accepted")

def deleteOrder(request):
    return HttpResponse("deleted")