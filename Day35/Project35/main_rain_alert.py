# https://home.openweathermap.org/
# https://openweathermap.org/forecast5
# https://openweathermap.org/current
# https://home.openweathermap.org/api_keys
# https://www.latlong.net/
# https://jsonviewer.stack.hu/
# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
# https://www.ventusky.com/

# https://login.twilio.com/   bayramguney@yahoo.com     Herseybizimicinolmali55@     code=K6ZR23YRSE1GJ25FBY5MQCXB
# https://www.twilio.com/docs/messaging/quickstart/python    SMS sent application
# phone number = +18557852224
import requests
from twilio.rest import Client
import os

api_key = "045476a18f4e7fba503ef609e7f2b4c0"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = 'ACc7609003a07cc5e56002d05cdebe45ea'      # from trilio
auth_token = 'd0e52b8581e0a8943760f219f8c586ed'
# https://api.openweathermap.org/data/2.5/weather?q=New%20York,US&appid=045476a18f4e7fba503ef609e7f2b4c0

# https://api.openweathermap.org/data/2.5/forecast?lat=74.006&lon=40.7143&appid=45476a18f4e7fba503ef609e7f2b4c0

MY_LAT = 25.761681
MY_LONG = -80.191788

parameters = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_ENDPOINT,params=parameters)
response.raise_for_status()
data = response.json()
will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data ["weather"][0]["id"]   # this is the code for weather condition from API docs
    if int(condition_code) < 700:
        will_rain = True
    if will_rain:
        client = Client(account_sid,auth_token)
        message = client.messages.create(
            body="It s going to rain today. Remember to take umbrella",
            from_="+18557852224",
            to="+17186403225"
        )
        print(message.status)


# pythonanywhere.com to run in cloud
# https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/