from django.shortcuts import render
from .models import *

def home(request):
    context = {}
    return render(request, 'data_entry/home.html', context)

def collectData(request):
    if request.method == 'POST':
        weather = request.POST['weather']
        temperature = request.POST['temperature']
        driver = request.POST['driver']
        location = request.POST['location']
        track = request.POST['track']
        fast_lap = request.POST['fast_lap']
        tires = request.POST['tires']
        tire_condition = request.POST['tire_condition']
        engine = request.POST['engine']
        software = request.POST['software']
        comments = request.POST['comments']

        context = {
            'weather': weather,
            'temperature': temperature,
            'driver': driver,
            'location': location,
            'track': track,
            'fast_lap': fast_lap,
            'tires': tires,
            'tire_condition': tire_condition,
            'engine': engine,
            'software': software,
            'comments': comments,
        }

        Test.objects.create(
            weather = weather,
            temperature = temperature,
            driver = driver,
            location = location,
            track = track,
            fast_lap = fast_lap,
            tires = tires,
            tire_condition = tire_condition,
            engine = engine,
            software = software,
            comments = comments
        )

        message = 'Data has been recorded'

        return render(request, 'data_entry/collectdata.html', message)

    else:
        context = {}
        return render(request, 'data_entry/collectdata.html', context)

def viewData(request):
    context = {}
    return render(request, 'data_entry/viewdata.html', context)

def createUser(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subteam = request.POST['subteam']

        context = {
            'name': name,
            'email': email,
            'subteam': subteam,
        }

        if Person.objects.filter(email=email).exists():
            message = "User already exist"
            context = {
                'message'
            }
            return render(request, 'data_entry/createuser.html', context)

        else:
            Person.objects.create(
                name = name,
                email = email,
                subteam = subteam,
            )

            message = 'User has been created'

            return render(request, 'data_entry/createuser.html', context)

    else:
        context = {}
        return render(request, 'data_entry/createuser.html', context)
