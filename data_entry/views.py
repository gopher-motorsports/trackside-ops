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
				entry.is_deleted = request.POST.get('is_deleted', False)
				entry.flagged = request.POST.get('flagged', False)
				entry.date = request.POST.get('date')
				entry.time = request.POST.get('time')
				entry.chassis = request.POST.get('chassis')
				entry.car = request.POST.get('car')
				entry.driver = request.POST.get('driver')
				entry.motor = request.POST.get('motor')
				entry.motor_comments = request.POST.get('motor_comments')
				entry.location = request.POST.get('location')
				entry.drive_day_lead = request.POST.get('drive_day_lead')
				entry.track = request.POST.get('track')
				entry.weather = request.POST.get('weather')
				entry.air_temp = request.POST.get('air_temp')
				entry.track_temp = request.POST.get('track_temp')
				entry.temperature_unit = request.POST.get('temperature_unit')
				entry.wind_direction = request.POST.get('wind_direction')
				entry.wind_speed = request.POST.get('wind_speed')
				entry.tires = request.POST.get('tires')
				entry.fl_tire_serial_number = request.POST.get('fl_tire_serial_number')
				entry.fl_tire_condition = request.POST.get('fl_tire_condition')
				entry.fr_tire_serial_number = request.POST.get('fr_tire_serial_number')
				entry.fr_tire_condition = request.POST.get('fr_tire_condition')
				entry.bl_tire_serial_number = request.POST.get('bl_tire_serial_number')
				entry.bl_tire_condition = request.POST.get('bl_tire_condition')
				entry.br_tire_serial_number = request.POST.get('br_tire_serial_number')
				entry.br_tire_condition = request.POST.get('br_tire_condition')
				entry.data_file_link = request.POST.get('data_file_link')
				entry.comments = request.POST.get('comments')
				context = {
					'is_deleted':entry.is_deleted,
					'flagged':entry.flagged,
					'date':entry.date,
					'time':entry.time,
					'chassis':entry.chassis,
					'car':entry.car,
					'driver':entry.driver,
					'motor':entry.motor,
					'motor_comments':entry.motor_comments,
					'location':entry.location,
					'drive_day_lead':entry.drive_day_lead,
					'track':entry.track,
					'weather':entry.weather,
					'air_temp':entry.air_temp,
					'track_temp':entry.track_temp,
					'temperature_unit':entry.temperature_unit,
					'wind_direction':entry.wind_direction,
					'wind_speed':entry.wind_speed,
					'tires':entry.tires,
					'fl_tire_serial_number':entry.fl_tire_serial_number,
					'fl_tire_condition':entry.fl_tire_condition,
					'fr_tire_serial_number':entry.fr_tire_serial_number,
					'fr_tire_condition':entry.fr_tire_condition,
					'bl_tire_serial_number':entry.bl_tire_serial_number,
					'bl_tire_condition':entry.bl_tire_condition,
					'br_tire_serial_number':entry.br_tire_serial_number,
					'br_tire_condition':entry.br_tire_condition,
					'data_file_link':entry.data_file_link,
					'comments':entry.comments
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
			print(request)
			is_deleted = request.POST.get('is_deleted', False)
			flagged = request.POST.get('flagged', False)
			date = request.POST.get('date')
			time = request.POST.get('time')
			chassis = request.POST.get('chassis')
			car = request.POST.get('car')
			driver = request.POST.get('driver')
			motor = request.POST.get('motor')
			motor_comments = request.POST.get('motor_comments')
			location = request.POST.get('location')
			drive_day_lead = request.POST.get('drive_day_lead')
			track = request.POST.get('track')
			weather = request.POST.get('weather')
			air_temp = request.POST.get('air_temp')
			track_temp = request.POST.get('track_temp')
			temperature_unit = request.POST.get('temperature_unit')
			wind_direction = request.POST.get('wind_direction')
			wind_speed = request.POST.get('wind_speed')
			tires = request.POST.get('tires')
			fl_tire_serial_number = request.POST.get('fl_tire_serial_number')
			fl_tire_condition = request.POST.get('fl_tire_condition')
			fr_tire_serial_number = request.POST.get('fr_tire_serial_number')
			fr_tire_condition = request.POST.get('fr_tire_condition')
			bl_tire_serial_number = request.POST.get('bl_tire_serial_number')
			bl_tire_condition = request.POST.get('bl_tire_condition')
			br_tire_serial_number = request.POST.get('br_tire_serial_number')
			br_tire_condition = request.POST.get('br_tire_condition')
			data_file_link = request.POST.get('data_file_link')
			comments = request.POST.get('comments')
			context = {
				'is_deleted':is_deleted,
				'flagged':flagged,
				'date':date,
				'time':time,
				'chassis':chassis,
				'car':car,
				'driver':driver,
				'motor':motor,
				'motor_comments':motor_comments,
				'location':location,
				'drive_day_lead':drive_day_lead,
				'track':track,
				'weather':weather,
				'air_temp':air_temp,
				'track_temp':track_temp,
				'temperature_unit':temperature_unit,
				'wind_direction':wind_direction,
				'wind_speed':wind_speed,
				'tires':tires,
				'fl_tire_serial_number':fl_tire_serial_number,
				'fl_tire_condition':fl_tire_condition,
				'fr_tire_serial_number':fr_tire_serial_number,
				'fr_tire_condition':fr_tire_condition,
				'bl_tire_serial_number':bl_tire_serial_number,
				'bl_tire_condition':bl_tire_condition,
				'br_tire_serial_number':br_tire_serial_number,
				'br_tire_condition':br_tire_condition,
				'data_file_link':data_file_link,
				'comments':comments,
			}
			Drives.objects.create(
			   is_deleted=is_deleted,
				flagged=flagged,
				date=date,
				time=time,
				chassis=chassis,
				car=car,
				driver=driver,
				motor=motor,
				motor_comments=motor_comments,
				location=location,
				drive_day_lead=drive_day_lead,
				track=track,
				weather=weather,
				air_temp=air_temp,
				track_temp=track_temp,
				temperature_unit=temperature_unit,
				wind_direction=wind_direction,
				wind_speed=wind_speed,
				tires=tires,
				fl_tire_serial_number=fl_tire_serial_number,
				fl_tire_condition=fl_tire_condition,
				fr_tire_serial_number=fr_tire_serial_number,
				fr_tire_condition=fr_tire_condition,
				bl_tire_serial_number=bl_tire_serial_number,
				bl_tire_condition=bl_tire_condition,
				br_tire_serial_number=br_tire_serial_number,
				br_tire_condition=br_tire_condition,
				data_file_link=data_file_link,
				comments=comments,
			)
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
			entry = Drives.objects.get(id=entry_id)
			entry.is_deleted = True
			entry.save()
			# Drives.objects.filter(id=entry_id).delete()
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

def filter_data(request):
	if request.method == 'POST':
		param = request.POST.get('param')
		field = request.POST.get('field')
		if field == "":
			context = {'entries': Drives.objects.all()}
			return render(request, 'data_entry/viewdata.html', context)
		entries = []
		for i in Drives.objects.all():
			if str(param).lower() in str(getattr(i,field)).lower():
				entries.append(i)
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
