from django.shortcuts import render
from .models import Person, Test
import datetime
from .serializers import PersonSerializer, TestSerializer
from rest_framework import viewsets

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all().order_by('created_at')
    serializer_class = TestSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer

"""
    Home Page

"""
def home(request):
    context = {}
    return render(request, 'data_entry/home.html', context)


"""
    Data Log Page

    if a POST request is received:
        Check if the entry is being loaded -> Get entry_id and display data
        Check if the entry is being updated -> Update fields and save entry
    otherwise load empty data log form

"""
def collectData(request):
    if request.method == 'POST':
        # if the request contains an entry ID
        # an entry is being updated or loaded to the form
        if request.POST['entry_id']:
            # check if the entry is being updated or loaded
            method = request.POST['method']
            # entry is being loaded
            if method == "load":
                entry_id = request.POST['entry_id']
                entry = Test.objects.get(id=entry_id)
                # format personnel array to a string; needed to display data correctly
                personnel = entry.personnel
                personnel = ','.join(personnel)

                # format date; needed to display correct date
                date_time_str = str(entry.created_at)
                date_time_str = date_time_str[:-6]
                date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
                date = str(date_time_obj.date())
                context = {
                    'entry': entry,
                    'personnel': personnel,
                    'date': date,
                    }
                return render(request, 'data_entry/collectdata.html', context)
            # entry is being updated
            else:
                entry_id = request.POST['entry_id']
                entry = Test.objects.get(id=entry_id)

                # update fields
                entry.weather = request.POST['weather']
                entry.temperature = request.POST['temperature']
                entry.driver = request.POST['driver']
                entry.location = request.POST['location']
                entry.track = request.POST['track']
                entry.fast_lap = request.POST['fast_lap']
                entry.tires = request.POST['tires']
                entry.tire_condition = request.POST['tire_condition']
                entry.engine = request.POST['engine']
                entry.software = request.POST['software']
                entry.comments = request.POST['comments']
                personnel = []
                for person in request.POST['personnel'].replace(' ', '').split(','):
                    if Person.objects.filter(name=person).exists():
                        personnel.append(person)
                    else:
                        message = 'No user found with name ' + person
                        return render(request, 'data_entry/collectdata.html', {'message': message})
                
                entry.personnel = personnel


                context = {
                    'weather': entry.weather,
                    'temperature': entry.temperature,
                    'driver': entry.driver,
                    'location': entry.location,
                    'track': entry.track,
                    'fast_lap': entry.fast_lap,
                    'tires': entry.tires,
                    'tire_condition': entry.tire_condition,
                    'engine': entry.engine,
                    'software': entry.software,
                    'comments': entry.comments,
                    'personnel': entry.personnel,
                }

                # save updated entry
                entry.save()

                message = 'Data has been updated'
                return render(request, 'data_entry/collectdata.html', {'message': message})
        
        # New entry
        # Get information from fields and create a new database entry
        # Validate users and display a success or an error message
        else:
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

"""
    View Data Page

    if a POST request is received:
        An entry is being deleted
        TODO: A search has been made
    otherwise load database entries

"""
def viewData(request):
    if request.method == 'POST':
        method = request.POST['method']
        # delete entry from database
        if method == "delete":
            entry_id = request.POST['entry_id']
            Test.objects.filter(id=entry_id).delete()
            entries = Test.objects.all()
            context = {'entries': entries}
            return render(request, 'data_entry/viewdata.html', context)
        
        # filter entries
        # TODO
        # Following code is a rough idea. 
        # Test.objects.filter might be a better idea

        # if method == "filter":
        #     param = request.POST['param']
        #     search = request.POST['search']
        #     entries = Test.objects.all()
        #     filtered_entries = []
        #     for entry in entries:
        #         if entry.search == param:
        #             filtered_entries.append(entry)

    # load all entries   
    else:
        entries = Test.objects.all()
        context = {'entries': entries}
        return render(request, 'data_entry/viewdata.html', context)


"""
    Create User Page

    Create a new user. Cannot create a new user if email has already been used.
    If a POST request is received create a new user. Otherwise, load the create user form

"""
def createUser(request):
    if request.method == 'POST':
        # Get new user fields
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

        # check if email has already been used and return error
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
