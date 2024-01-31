from fastapi import FastAPI
import requests


api_key = 'your_OpenWeather_Key'

app = FastAPI()




@app.get('/city/{city_name}/')
def get_city(city: str):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={5}&appid={api_key}'
    
    request = requests.get(url)
    if request.status_code == 200:
        weather_data = request.json()
        return weather_data
    else:
        return {'message':' error '}


@app.get('/weather/{latitude}{longitude}')
def get_weather(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    
    air_url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}'
    
    week_forecast = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}'
    
    weather_request = requests.get(url)
    air_request = requests.get(air_url)
    week_request = requests.get(week_forecast)
    
    result = [{'forecast': weather_request.json()},
              {'air_quality': air_request.json()},
              {'week_forecast': week_request.json()}]
    
    return result

