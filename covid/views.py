from django.shortcuts import render
from .corona_api import CoronaStats 
# Create your views here.
c1 = CoronaStats()
def home(request):
    data = {
        "world":c1.wholeWorld()
    }
    return render(request, "pages/home.html",data)

def europe(request):
    data = {
        "europe":c1.continentFilter("Europe")
    }
    return render(request,"pages/europe.html",data)

def asia(request):
    data = {
        "asia": c1.continentFilter("Asia")
    }
    return render(request, "pages/asia.html", data)

def africa(request):
    data = {
        "africa": c1.continentFilter("Africa")
    }
    return render(request, "pages/africa.html", data)

def australia_oceania(request):
    data = {
        "australia_oceania": c1.continentFilter("Australia-Oceania")
    }
    return render(request, "pages/australia-oceania.html", data)

def north_america(request):
    data = {
        "north_america": c1.continentFilter("North America")
    }
    return render(request, "pages/north-america.html", data)

def south_america(request):
    data = {
        "south_america": c1.continentFilter("South America")
    }
    return render(request, "pages/south-america.html", data)
