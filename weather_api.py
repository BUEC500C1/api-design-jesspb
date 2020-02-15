import flask
import json
from flask import jsonify
import requests
from flask import request
from extra_func import getCityFromCode
from extra_func import getCityFromAirport
from config import api_key

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def call_api(city):
    # openweathermap api call
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key

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


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Airport Weather API</h1>
<p>ENG EC 500 - Building Software Homework 2</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1', methods=['GET'])
def api_all():

     #  gets ident code or airport name from url
    if 'code' in request.args:
        code = request.args['code']
        city = getCityFromCode(code)
    elif 'airport' in request.args:
        airport = request.args['airport']
        city = getCityFromAirport(airport)
    else:
        return "<h1>Error</h1><p>Please enter an airport code or name.</p>"

    if city == "":
        return "<h1>Error</h1><p>City could not be found for airport code or name</p>"

    weather = call_api(city)

    if weather == -1:
        return "<h1>Error</h1><p>City could not be found</p>"
    else:
        return jsonify(weather)


app.run()
