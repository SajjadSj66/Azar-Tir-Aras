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
    path('service/', service, name="service"),
    path('aboutus/', aboutus, name="aboutus"),
]
