import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import csv

names = [] #List to store name of the product
prices = [] #List to store price of the product
url = "https://www.bcv.org.ve/tasas-informativas-sistema-bancario"
response = requests.get(url)

content = response.text
soup = BeautifulSoup(content, features = "html.parser")
for div in soup.findAll('div', attrs = {'row recuadrotsmc'}):
  name = div.find('span')
  price = div.find('strong')
  names.append(name.text)
  prices.append(price.text)

df = pd.DataFrame({'Name of coin':names, 'Prices':prices})
df.to_csv('divisas_price.csv',index = False, encoding = 'utf-8')

csvFilePath = 'divisas_price.csv'
jsonFilePath = 'divisas.json'
jsonArray = []
with open(csvFilePath, encoding = 'utf-8') as csvf:
  csvReader = csv.DictReader(csvf)
  for row in csvReader:
    jsonArray.append(row)
with open(jsonFilePath, encoding = 'utf-8') as jsonf:
 jsonString = json.dumps(jsonArray, indenr = 4)
 json.write(jsonString)


