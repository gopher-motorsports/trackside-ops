x = ['is_deleted','flagged','date','time','chassis','car','driver','motor','motor_comments','location','drive_day_lead','track','weather','air_temp','track_temp','temperature_unit','wind_direction','wind_speed','tires','fl_tire_serial_number','fl_tire_condition','fr_tire_serial_number','fr_tire_condition','bl_tire_serial_number','bl_tire_condition','br_tire_serial_number','br_tire_condition','data_file_link','comments','created_at']
# for i in x:
# 	print("'"+i+"'"+":"+i+",")

# for i in x:
# 	print(i+"="+i+",")

# for i in x:
# 	print("<b>"+i+":</b> {{entry."+i+"}}<br>")	

# for i in x:
# 	print("document.getElementById('"+i+"').value = '{{entry."+i+"}}';")

for i in x:
	print('<option value="'+i+'">'+i+'</option>')