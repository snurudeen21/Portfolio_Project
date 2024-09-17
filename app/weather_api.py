import requests
import json

def weather_api():

	try:
		api_request = requests.get("https://www.meteosource.com/api/v1/free/point?place_id=" + "London" "&sections=current%2Chourly\
							            &language=en&units=auto&key=x4r7nfopqo4fyp287xa6pq08fgbtyl7lxsuu9f1a")
		api = json.loads(api_request.content)
		city = api[0]['ReportingArea']
		quality = api[0]['AQI']
		category = api[0]['Category']['Name']

  
	except Exception as e:	
		api = "Error..."