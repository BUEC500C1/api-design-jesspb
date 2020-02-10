import flask
import json
from flask import jsonify
import requests
from flask import request
from extra_func import getAirportFromCode
from config import api_key

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def call_api(city):
    # openweathermap api call
    url = "api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key

    response = requests.get(url).json()

    if (response["cod"] != "404") & (response["cod"] != "400"):

        weath = response['main']
        desc = response['weather'][0]['description']
        temp = weath['temp']-273.13
        feels_like = weath['feels_like']-273.13
        humidity = weath['humidity']

        weather = [

            {
            'Descripton': desc,
            'Temperature (C)': temp,
            'Feels Like (C)': feels_like,
            'Humidity': humidity}
        ]
        return weather

    else:
        print("Error: Could not find city")
        return -1
