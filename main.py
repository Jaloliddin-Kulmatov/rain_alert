import requests
from twilio.rest import Client

account_sid = ""
auth_token = ""
api_key = ""
End_point_API = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {"lat": 1.352083,
              "lon": 103.819839,
              "appid": api_key,
              "cnt": 4}
response = requests.get(url=End_point_API, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for each_hour in data["list"]:
    weather_id = each_hour["weather"][0]["id"]
    time = each_hour["dt_txt"]
    if weather_id < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's going to rain today. Remember to bring an ☔️",
        to="whatsapp:+821082694111"
    )
    print(message.status)
