from newsapi import NewsApiClient
import json
import csv
import requests
import pandas as pd


request = requests.get('https://fakerapi.it/api/v1/companies?_quantity=50')

data = json.loads(request.content)
data_file = pd.json_normalize(data)
data_file.to_csv("fake.csv")
print(data)


















                          