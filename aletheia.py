import requests
import pandas as pd
import json


class Aletheia:

  def __init__(self,header=None, aletheia=None):
    self.headers = {'key':'53BCA326AD154E77B4C6B11CBB2C8EEF'}
    
  
  def collect(self):
    self.aletheia = requests.get('https://api.aletheiaapi.com/Crypto?symbol=BTC',headers=self.headers)
    data = json.loads(self.aletheia.content)
    data_file = pd.json_normalize(data)
    data_file.to_csv("aletheia.csv")

    





