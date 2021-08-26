import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# Use your own api_keys and other details
OWM_api="https://api.openweathermap.org/data/2.5/onecall"
api_keys="a5915dede361ef61c32c9e24b49fb323"
account_sid = "AC10294f136641b91d8c0e198d7adf0545"
auth_token = "8ed5d2b11eea5898fd74316e3d7b9a46"

weather_parameters={
    "lat":22.565571,
    "lon":88.370209,
    "appid":api_keys,
    "exclude":"current,minutely,daily",

}

response=requests.get(OWM_api,params=weather_parameters)
weather_data=response.json()
weather_slice=weather_data["hourly"][:12]
will_it_rain= False
for hour_data in weather_slice:
    condition_code=hour_data["weather"][0]["id"]
    if condition_code<700:
        will_it_rain=True

if will_it_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain.Don't forget to take your Umbrella.",
                     from_='+16783378253',
                     to=input("Enter your phone number:+91")
                 )
    print(message.status)   
