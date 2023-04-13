from django.shortcuts import render
from missions.models import Mission

def home(request):
    return render(request, "home.html")

def mission_list(request):
    missions = Mission.objects.all()

    context = {
        "missions": missions,
    }

    return render(request, "mission_list.html", context)
