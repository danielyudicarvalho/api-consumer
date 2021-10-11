import requests
import pandas as pd
import json
from converter import *


class Aletheia:

  def __init__(self,header=None, aletheia=None,converter=None):
    self.headers = {'key':'53BCA326AD154E77B4C6B11CBB2C8EEF'}
    self.converter = Converter()
    
  
  def collect(self):
    self.aletheia = requests.get('https://api.aletheiaapi.com/Crypto?symbol=BTC',headers=self.headers)
    self.converter.convert(self.aletheia.content)
   

    





