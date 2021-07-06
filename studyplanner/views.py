from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Functions and classes mapped to urls

def index(request):
    return HttpResponse("Welcome to Study Planner")

def monday(request):
    return HttpResponse("Today I'm learning Django")

def weekly_timetable(request, day):
    text = ""
    if day == "monday":
        text = "Today I'm learning Django"
    elif day == "tuesday":
        text = "Data Science Day"

    return HttpResponse(text)