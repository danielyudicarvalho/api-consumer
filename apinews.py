from newsapi import NewsApiClient
from converter import *
import json
import csv
import pandas as pd



class News:

  def __init__(self, newsapi=None,bitcoinsNews=None,converter = None):
    self.newsapi = NewsApiClient(api_key='468dc2b9fc9f4ad08c977058f3623b8a')
    self.converter = Converter()


  def collect(self):
    self.bitcoinsNews = self.newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2021-10-10',
                                      to='2021-03-10',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
    
    data = json.dumps(self.bitcoinsNews)
    self.converter.convert(data)
    df_json = json.loads(data)
    df = pd.json_normalize(df_json)
    df.to_csv('news.csv')
    


  


