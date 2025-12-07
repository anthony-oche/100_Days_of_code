import requests

API_KEY = "699493f32af07dc843e3d9e2a8e365be"
MY_LAT = 40.712776
MY_LONG = -74.005974

weather_params= {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_list = weather_data['list']

#Todo: My solution


# weather_id = 0
# for hour_data in weather_list:
#     for weather in hour_data["weather"]:
#         weather_id = weather["id"]
# if weather_id < 700:
#     print("Bring an Umbrella")


#Todo: Angela solution
will_rain = False
for hour_data in weather_list:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")


