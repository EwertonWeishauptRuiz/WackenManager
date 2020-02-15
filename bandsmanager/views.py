from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, band_id):
    return HttpResponse("You're looking at band {}.".format(band_id))

def results(request, band_id):
    response = "You're looking at the results of band {}.".format(band_id)
    return HttpResponse(response)

def vote(request, band_id):
    return HttpResponse("You're voting on band {}.".format(band_id))
