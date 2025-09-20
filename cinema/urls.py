from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.home, name="home"),
    path("market/", views.market, name="market"),
    path("about/", views.about, name="about"),
    path("read/", views.read, name="read"),
    path("customers/", views.view_customers, name="customers"),
]

