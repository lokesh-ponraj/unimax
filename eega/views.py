from django.shortcuts import render

# Create your views here.
def check(request):
    return render(request, 'eega/template.html')

def homePage(request):
    return render(request, 'eega/home.html')

def login(request):
    return render(request, 'eega/login.html')

def distributers(request):
    return render(request, 'eega/distributers.html')

def dealers(request):
    return render(request, 'eega/dealers.html')

def fleets(request):
    return render(request, 'eega/fleets.html')

def vehicles(request):
    return render(request, 'eega/vehicles.html')

def gpsDevices(request):
    return render(request, 'eega/gpsdevices.html')

def rawData(request):
    return render(request, 'eega/rawdata.html')

def alerts(request):
    return render(request, 'eega/alert.html')

def reports(request):
    return render(request,'eega/reports.html')

def fieldEngineer(request):
    return render(request, 'eega/fieldEngineer.html')

def configurations(request):
    return render(request, 'eega/configurations.html')

def geofence(request):
    return render(request, 'eega/geofence.html')
