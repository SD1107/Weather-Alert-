import requests
from twilio.rest import Client
import os
from  dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)

api_key=os.getenv("API_KEY")
weather_parameretrs={
    "lat":23.344101,
    "lon":85.309563,
    "appid":api_key,
    "cnt":4,
}


count=1
response=requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast",params=weather_parameretrs)
#print(response)
response.raise_for_status()
data=response.json()
print(data)


for i in range(weather_parameretrs["cnt"]):
    weather_id=data["list"][i]["weather"][0]["id"]
    # description=data["list"][0]["weather"][0]["description"]
    if(int(weather_id)<700):
        count=0
        break
# print(f"The weather id is {weather_id1} and the description is {description1}")
# feels_like=data[]


if count==0:
    message = client.messages.create(
    body=f"It's going to rain today in {data["city"]["name"]}. Bring an ☂️.Have a nice day ahead!\n\n~Soumyadeep Dey😎",
    from_="+19894798783",
    to="+918334922370",
    )
else:
    message = client.messages.create(
    body=f"It's not going to rain today in {data["city"]["name"]}. No need to bring an ☂️.Have a nice day ahead!\n\n~Soumyadeep Dey😎",
    from_=os.getenv("FROM_MOB"),
    to=os.getenv("TO_MOB"),
    )
print(message.status)


