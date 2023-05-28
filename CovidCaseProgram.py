import requests
import os
import csv
import pygsheets
import pandas as pd

url = 'https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/ed270bb8-340b-41f9-a7c6-e8ef587e6d11/download/covidtesting.csv'
r = requests.get(url, allow_redirects=True)

open('Covid Data.csv', 'wb').write(r.content)


col = [0,6,7]

with open("Covid Data.csv") as fr, open("Covid Data Updated.csv","w",newline="") as fw:
    cr = csv.reader(fr)
    cw = csv.writer(fw)
    cw.writerows([row[i] for i in col] for row in cr)

gc = pygsheets.authorize(service_file='./covid-cases-project-new-83175c29a1cb.json')
df = pd.read_csv('Covid Data.csv', usecols = ['Reported Date','Confirmed Positive','Deaths'], low_memory = True)
sh = gc.open('CovidCasesData')
wks = sh[0]
wks.set_dataframe(df,(1,1))
df = pd.DataFrame()
df['brian'] = ['John', 'Steve', 'Sarah']
sh = gc.open('CovidCasesData')
wks = sh[0]
wks.set_dataframe(df,(10,10))

print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
print("PATH:", os.environ.get('PATH'))

