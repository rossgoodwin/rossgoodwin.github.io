import csv
import json
from collections import defaultdict
import datetime
import calendar
import StringIO
import requests

response = requests.get('https://docs.google.com/spreadsheets/d/1W2e4HI2pCrI2zTISdif4D4rcKJ_2K2Lq07E-fr-ZGQ0/pub?gid=1348098975&single=true&output=csv')

with open('projects.csv', 'w') as outfile:
	outfile.write(response.text)

fileObj = open('projects.csv', 'r')

reader = csv.DictReader(fileObj)

projList = []

for row in reader:
	# print row.keys()
	projList.append(row)

fileObj.close()

def get_date(projObj):
	m, d, y = map(int, projObj['Date of Completion'].split('/'))
	dateObj = datetime.datetime(y, m, d, 0, 0)
	return -(dateObj - datetime.datetime(1970,1,1)).total_seconds()

projList = sorted(projList, key=get_date)


with open('projects.json', 'w') as outfile:
	json.dump(projList, outfile)

