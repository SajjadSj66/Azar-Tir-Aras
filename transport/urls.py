from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact_view, name="contact"),
    path('tarkibi/', tarkibi, name="tarkibi"),
    path('ship/', ship, name="ship"),
    path('truck/', truck, name="truck"),
    path('train/', train, name="train"),
    path('airplane/', airplane, name="airplane"),
    path('hamle_asli/', hamle_asli, name="hamle_asli"),
    path('international/', international, name="international"),
    path('roads/', roads, name="roads"),
    path('service_import/', service_import, name="service_import"),
    path('service_export/', service_export, name="service_export"),
    path('service_new/', service_new, name="service_new"),
    path('service_tarkhis/', service_tarkhis, name="service_tarkhis"),
    path('service_umurgomroki/', service_umurgomroki, name="service_umurgomroki"),
    path('aboutus/', aboutus, name="aboutus"),
]
