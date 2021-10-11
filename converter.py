import pandas as pd
import json
import random
import string


class Converter:
  def __init__(self,index=None):
    self.index = 1

  def convert(self,data):
    data_json = json.loads(data)
    data_file = pd.json_normalize(data_json)
    letter = string.ascii_lowercase
    hashg = ''.join(random.choice(letter) for i in range(5))
    data_file.to_csv("{}.csv".format(hashg))


