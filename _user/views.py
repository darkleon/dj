from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


adef index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def item(request):
    return HttpResponse("11111.")
