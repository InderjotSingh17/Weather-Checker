import requests
from django.shortcuts import render

def get_weather(request):
    weather_data = None
    error_message = None

    if 'city' in request.GET:
        city = request.GET['city']
        api_key = "79913d8966120c4168272cd0a4b719fa"  
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.json()
        else:
            error_message = "City not found. Please try again."

    return render(request, 'home.html', {'weather_data': weather_data, 'error_message': error_message})
