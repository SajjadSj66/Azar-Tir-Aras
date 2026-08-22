from django.shortcuts import render, redirect
from .forms import ContactForm
# Create your views here.

def index(request):
    return render(request, "landing.html")

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = ContactForm()
    return render(request, "callus.html", {"form": form})

def airplane(request):
    return render(request, "airplane.html")

def ship(request):
    return render(request, "ship.html")

def truck(request):
    return render(request, "truck.html")

def train(request):
    return render(request, "train.html")

def tarkibi(request):
    return render(request, "tarkibi.html")

def service(request):
    return render(request, "service.html")

def aboutus(request):
    return render(request, "about.html")