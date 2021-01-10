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
        personnel = []
        for person in request.POST['personnel'].replace(' ', '').split(','):
            if Person.objects.filter(name=person).exists():
                personnel.append(person)
            else:
                message = 'No user found with name ' + person
                return render(request, 'data_entry/collectdata.html', {'message': message})


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
            'personnel': personnel,
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
            comments = comments,
            personnel = personnel
        )

        message = 'Data has been recorded'

        return render(request, 'data_entry/collectdata.html', {'message': message})

    else:
        context = {}
        return render(request, 'data_entry/collectdata.html', context)

def viewData(request):
    #when they want to do filters
    if request.method == 'POST':
        filter = request.POST['filter']
        param = request.POST['param']
        entries = Test.objects.all()
        filtered_entires = []
        for entry in entries:
            #test is table name
            if Test.object.filter(entry.filter==param):
                filtered_entires.append(entry)   
        context = {'filtered_entries': filtered_entries}
        return render(request, 'data_entry/viewdata.html', context)

    else:     
        entries = Test.objects.order_by('-created_at')
        context = {'entries': entries}
        return render(request, 'data_entry/viewdata.html', context)

def createUser(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subteam = request.POST['subteam']
        phone = request.POST['phone']
        licensed = request.POST['licensed']

        context = {
            'name': name,
            'email': email,
            'subteam': subteam,
            'phone': phone,
            'licensed': licensed,
        }

        if Person.objects.filter(email=email).exists():
            return render(request, 'data_entry/createuser.html', {'email':email})

        else:
            Person.objects.create(
                name = name,
                email = email,
                subteam = subteam,
                phone = phone,
                licensed = licensed,
            )

            return render(request, 'data_entry/createuser.html', {'name':name})

    else:
        context = {}
        return render(request, 'data_entry/createuser.html', context)
