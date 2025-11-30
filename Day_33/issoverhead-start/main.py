import requests
from datetime import datetime
import smtplib
import time

my_email = "ocheanthonyowoicho@gmail.com"
password = "phvvqbwuzakvhhma"
MY_LAT = 8.879310
MY_LONG = 7.235260

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    return None


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    #If the ISS is close to my current position
    if time_now >= sunset or time_now <= sunrise:
        return True
    return None

# Then email me to tell me to look up.
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="rochi.switch@gmail.com",
                                msg="Subject:ISS IS OVERHEAD\n\nLook up")
# BONUS: run the code every 60 seconds.



