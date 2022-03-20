from django.shortcuts import render, redirect
from .models import Person, Drives
import datetime
from .serializers import PersonSerializer, DrivesSerializer
from rest_framework import viewsets


class DrivesViewSet(viewsets.ModelViewSet):
    queryset = Drives.objects.all().order_by('created_at')
    serializer_class = DrivesSerializer


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
                entry = Drives.objects.get(id=entry_id)
                # format date; needed to display correct date
                date_time_str = str(entry.created_at)
                date_time_str = date_time_str[:-6]
                date_time_obj = datetime.datetime.strptime(
                    date_time_str, '%Y-%m-%d %H:%M:%S.%f')
                date = str(date_time_obj.date())
                context = {
                    'entry': entry,
                    'date': date,
                }
                return render(request, 'data_entry/edit_drives.html', context)
            # entry is being updated
            else:
                entry_id = request.POST['entry_id']
                entry = Drives.objects.get(id=entry_id)

                # update fields
                entry.motor_num = request.POST['motor_num']
                entry.car_type = request.POST['car_type']
                entry.is_racespec = request.POST['is_racespec']
                entry.weather = request.POST['weather']
                entry.track_temp = request.POST['track_temp']
                entry.air_temp = request.POST['air_temp']
                entry.driver = request.POST['driver']
                entry.location = request.POST['location']
                entry.is_dyno = request.POST['is_dyno']
                entry.track = request.POST['track']
                entry.tires = request.POST['tires']
                entry.tire_serial_number = request.POST['tire_serial_number']
                entry.date = request.POST['date']
                entry.tire_condition = request.POST['tire_condition']
                entry.engine = request.POST['engine']
                entry.comments = request.POST['comments']
                entry.drive_day_lead = request.POST['drive_day_lead']

                context = {
                    'motor_num': entry.motor_num,
                    'car_type': entry.car_type,
                    'is_racespec': entry.is_racespec,
                    'weather': entry.weather,
                    # 'temperature': entry.temperature,
                    'track_temp': entry.track_temp,
                    'air_temp': entry.air_temp,
                    'driver': entry.driver,
                    'location': entry.location,
                    'is_dyno': entry.is_dyno,
                    'track': entry.track,
                    'date': entry.date,
                    'tires': entry.tires,
                    'tire_serial_number': entry.tire_serial_number,
                    'tire_condition': entry.tire_condition,
                    'engine': entry.engine,
                    'comments': entry.comments,
                    'drive_day_lead': entry.drive_day_lead,
                }

                # save updated entry
                entry.save()

                # message = 'Data has been updated'
                # return render(request, 'data_entry/collectdata.html', {'message': message})
                return redirect('view_data')

        # New entry
        # Get information from fields and create a new database entry
        # Validate users and display a success or an error message
        else:
            motor_num = request.POST['motor_num']
            car_type = request.POST['car_type']
            is_racespec = request.POST['is_racespec']
            weather = request.POST['weather']
            track_temp = request.POST['track_temp']
            air_temp = request.POST['air_temp']
            driver = request.POST['driver']
            location = request.POST['location']
            is_dyno = request.POST['is_dyno']
            track = request.POST['track']
            tires = request.POST['tires']
            tire_serial_number = request.POST['tire_serial_number']
            date = request.POST['date']
            tire_condition = request.POST['tire_condition']
            engine = request.POST['engine']
            comments = request.POST['comments']
            drive_day_lead = request.POST['drive_day_lead']

            print("TRACK IS", track)

            context = {
                'motor_num': motor_num,
                'car_type': car_type,
                'is_racespec': is_racespec,
                'weather': weather,
                # 'temperature': temperature,
                'track_temp': track_temp,
                'air_temp': air_temp,
                'driver': driver,
                'location': location,
                'is_dyno': is_dyno,
                'track': track,
                'date': str(date),
                'tires': tires,
                'tire_serial_number': tire_serial_number,
                'tire_condition': tire_condition,
                'engine': engine,
                'comments': comments,
                'drive_day_lead': drive_day_lead,
            }

            Drives.objects.create(
                motor_num=motor_num,
                car_type=car_type,
                is_racespec=is_racespec,
                weather=weather,
                air_temp=air_temp,
                track_temp=track_temp,
                driver=driver,
                date=date,
                location=location,
                track=track,
                is_dyno=is_dyno,
                tires=tires,
                tire_serial_number=tire_serial_number,
                tire_condition=tire_condition,
                engine=engine,
                comments=comments,
                drive_day_lead=drive_day_lead
            )

            message = 'Data has been recorded'
            # return render(request, 'data_entry/collectdata.html', {'message': message})
            return redirect('view_data')
        # GET REQUEST
    else:
        context = {}
        return render(request, 'data_entry/enter_drives.html', context)


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
            Drives.objects.filter(id=entry_id).delete()
            entries = Drives.objects.all()
            context = {'entries': entries}
            return render(request, 'data_entry/viewdata.html', context)
        elif method == "filter":
            param = request.POST['param']
            hashTable = {
                "id": "id",
                "Date": "date",
                "Weather": "weather",
                "Temperature": "temperature",
                "Driver": "driver",
                "Location": "location",
                "Track": "track",
                "Fast Lap": "fast_lap",
                "Tires": "tires",
                "Tire Condition": "tire_condition",
                "Engine": "engine",
                "Software": "software",
                "Comments": "comments",
                "Created At": "created_at",
                "Personnel": "personnel"
            }
            search_param = request.POST['search']
            d = {
                hashTable[search_param]: param
            }
            entries = Drives.objects.filter(**d)
            context = {'entries': entries}
        return render(request, 'data_entry/viewdata.html', context)
    # load all entries
    else:
        entries = Drives.objects.all()
        context = {'entries': entries}
        return render(request, 'data_entry/viewdata.html', context)


"""
    Create User Page

    Create a new user. Cannot create a new user if email has already been used.
    If a POST request is received create a new user. Otherwise, load the create user form

"""


def viewTeam(request):
    if request.method == 'POST':
        method = request.POST['method']
        # delete entry from database
        if method == "delete":
            entry_id = request.POST['entry_id']
            Drives.objects.filter(id=entry_id).delete()
            entries = Drives.objects.all()
            context = {'entries': entries}
            return render(request, 'data_entry/viewdata.html', context)
        elif method == "filter":
            param = request.POST['param']
            hashTable = {
                "Name": "name",
                "Subteam": "subteam",
                "Email": "email",
                "Phone": "phone",
                "Licensed": "licensed",
            }
            search_param = request.POST['search']
            d = {
                hashTable[search_param]: param
            }
            entries = Drives.objects.filter(**d)
            context = {'entries': entries}
        return render(request, 'data_entry/viewteam.html', context)
    # load all entries
    else:
        entries = Drives.objects.all()
        context = {'entries': entries}
        return render(request, 'data_entry/viewteam.html', context)


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
            return render(request, 'data_entry/createuser.html', {'email': email})

        else:
            Person.objects.create(
                name=name,
                email=email,
                subteam=subteam,
                phone=phone,
                licensed=licensed,
            )

            return render(request, 'data_entry/createuser.html', {'name': name})

    else:
        context = {}
        return render(request, 'data_entry/createuser.html', context)
