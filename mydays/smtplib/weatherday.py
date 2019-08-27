#!/usr/local/bin/python3

from smtplib import SMTP_SSL
import pyowm
import os
from email.mime.text import MIMEText


def get_smtp_creds():
    return os.environ['SMTP_USERNAME'], os.environ['SMTP_PASSWORD']


def get_owm_apikey():
    return os.environ['OWM_APIKEY']

def get_todays_weather(apikey, location):
    owm = pyowm.OWM(apikey)
    observation = owm.weather_at_place(location)
    return observation.get_weather()


if __name__ == "__main__":
    smtp_username, smtp_password = get_smtp_creds()
    apikey = get_owm_apikey()
    with SMTP_SSL("smtp.fastmail.com" ) as smtp:
        smtp.login(smtp_username, smtp_password)
        msg = MIMEText(str(get_todays_weather(apikey, "Boston, US")))
        msg['From'] = "Chris Patti's Python Weather Robot <feoh@feoh.org>"
        msg['To'] = "cpatti@gmail.com"
        msg['Subject'] = "Today's Weather for Boston, MA"
        smtp.send_message(msg)
