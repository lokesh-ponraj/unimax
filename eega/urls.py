from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage,name='home'),
    path('login/', views.login, name='login'),
    path('channels/distributers/', views.distributers,name='distributers'),
    path('channels/dealers/', views.dealers,name='dealers'),
    path('channels/fleets/',  views.fleets,name='fleets'),
    path('channels/vehicles/', views.vehicles, name='vehicles'),
    path('channels/gpsdevices/',views.gpsDevices, name='gpsdevices'),
    path('channels/rawdata/',views.rawData, name='rawdata'),
    path('alerts/',views.alerts,name='alerts'),
    path('reports/', views.reports,name='reports'),
    path('fieldEngineer/',views.fieldEngineer, name='fieldEngineer'),
]
