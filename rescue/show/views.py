from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'show/index.html')


def drawing(request):
    return render(request, 'show/structural_drawing.html')


def evacuation(request):
    return render(request, 'show/evacuation_plan.html')
