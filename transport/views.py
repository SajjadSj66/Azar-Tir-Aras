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
    return render(request, "contactnew.html", {"form": form})

def hamle_asli(request):
    return render(request, "hamle-asli.html")

def airplane(request):
    return render(request, "hamle-havayi.html")

def ship(request):
    return render(request, "hamle-daryayi.html")

def truck(request):
    return render(request, "hamle-jadei.html")

def train(request):
    return render(request, "hamle-reyli.html")

def tarkibi(request):
    return render(request, "hamle-tarkibi.html")

def international(request):
    return render(request, "hamle.beynolmelal.html")

def roads(request):
    return render(request, "masirha.html")

def service_import(request):
    return render(request, "serviceimport.html")

def service_export(request):
    return render(request, "servicesexport.html")

def service_new(request):
    return render(request, "servicesnew.html")

def service_tarkhis(request):
    return render(request, "servicestarkhis.html")

def service_umurgomroki(request):
    return render(request, "servicesumurgomroki.html")

def aboutus(request):
    return render(request, "aboutnew.html")