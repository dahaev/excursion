from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("test Marmaris")

# Create your views here.
