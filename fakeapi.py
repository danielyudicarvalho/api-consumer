import requests
import json
import pandas as pd



class Fake:
  def __init__(self,request=None,key=None):
    self.key = {}



  def collect(self):
    self.request = requests.get('https://fakerapi.it/api/v1/companies?_quantity=50')
    data = json.loads(self.request.content)
    data_file = pd.json_normalize(data)
    data_file.to_csv("fake.csv")
   
  