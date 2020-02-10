import csv
import requests

def getCityFromCode(code):
    with open("airports/airports_csv.csv", 'r') as fileCSV:
        csvreader = csv.reader(fileCSV)
        for val in csvreader:
            if val[1] == ident:
                return val[10]
    return ""


#  finds airport name given an airport name
def getCityFroAirport(airport):
    with open("airports/airports_csv.csv", 'r') as filrCSV:
        csvreader = csv.reader(csvfile)
        for val in csvreader:
            if val[3] == airport_name:
                return val[10]
    return ""
