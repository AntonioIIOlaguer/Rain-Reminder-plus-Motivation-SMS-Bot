import os
import random
import json
import requests
from twilio.rest import Client
from my_params import *

#--------------------------------------Motivational Messaage----------------------------#    
with open("quotes_bank.json", "r") as file:
    all_quotes = json.loads(file.read())
with open("emoji_bank.json", "r") as file:
    all_emoji = json.loads(file.read())

quote_of_the_day = random.choice(all_quotes)
emoji_of_the_day = random.choice(all_emoji)

message_content = (f"{quote_of_the_day}\n{emoji_of_the_day}")
    

#----------------------------------------Rain_Checker---------------------------------------------#

parameter = {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "appid" : os.environ['OWM_API_KEY'],
    "exclude" : "current,minutely,daily"
}
#Access OpenWeather Data
response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameter)
response.raise_for_status()
weather_data = response.json()

#Taps unto the weather ID and checks if it's going to rain using IDs below 700 and then appends to a list of strings.
is_it_raining = False
for hour in range(12):
    for weather in weather_data["hourly"][hour]["weather"]:
        if weather["id"] < 700:
            is_it_raining = True
            break

if is_it_raining:
    message_content += f"\n\nOh and It's going to rain today! Don't forget to bring your umbrella.☂️"
    
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body=message_content,
                    from_=MY_TWILIO_NUM,
                    to=RECIPIENT_NUM,
                )
                