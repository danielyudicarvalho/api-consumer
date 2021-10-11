import requests
import json
import pandas as pd
from converter import *



class Fake:
  def __init__(self,request=None,key=None,converter= None):
    self.key = {}
    self.converter = Converter()



  def collect(self):
    self.request = requests.get('https://fakerapi.it/api/v1/companies?_quantity=50')
    self.converter.convert(self.request.content)
   
   
  