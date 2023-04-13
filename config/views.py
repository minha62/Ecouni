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

def mission_search(request):
    keyword = request.GET.get("keyword")

    if keyword is not None:
        missions = Mission.objects.filter(name__contains=keyword)
    else:
        missions = Mission.objects.none()

    context = {
        "missions": missions,
    }

    return render(request, "mission_search.html", context)