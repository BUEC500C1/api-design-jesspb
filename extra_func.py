import csv
import sys
import requests
import pytemperature

def getAirportFromCode(code)
    with open("airports/airports_csv.csv", 'r') as fileCSV:
        csvreader = csv.reader(fileCSV)
        
