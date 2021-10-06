import csv
import requests
import pandas as pd


data = json.dumps(bitcoinsNews)
data_file = open('data_file.csv', 'w')
csv_writer = csv.writer(data_file)

for item in data:
  csv_writer.writerow(item)

data_file.close()


#####################

    data = json.loads(self.aletheia.content)
    data_file = pd.json_normalize(data)
    data_file.to_csv("aletheia.csv")




