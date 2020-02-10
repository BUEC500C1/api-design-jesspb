import flask
import json
from flask import jsonify
import requests
from flask import request
from extra_func import getAirportFromCode

app = flask.Flask(__name__)
app.config["DEBUG"] = True
