import requests, smtplib
from datetime import datetime

my_email = 'lucjanoforpythono@gmail.com'
password = 'tylazhlsxqkujcth'

MY_LAT = 51.110550
MY_LONG = 17.038538

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
iss_postion = (iss_latitude, iss_longitude)
print(iss_postion)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now()

if time_now.hour > sunset or time_now < sunrise:
    if iss_latitude in range(41, 52) and iss_longitude in range(12, 23):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs='lucjanopavarotti@yahoo.com',
                                msg="Subject:ISS\n\nLook up!")



