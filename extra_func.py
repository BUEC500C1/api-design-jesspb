import csv
import requests

def getCityFromCode(code):
    with open("airports/airports_csv.csv", 'r') as fileCSV:
        csvreader = csv.reader(fileCSV)
        for val in csvreader:
            if val[1] == code:
                return val[10]
    return ""


#  finds airport name given an airport name
def getCityFromAirport(airport):
    with open("airports/airports_csv.csv", 'r') as fileCSV:
        csvreader = csv.reader(fileCSV)
        for val in csvreader:
            if val[3] == airport:
                return val[10]
    return ""
