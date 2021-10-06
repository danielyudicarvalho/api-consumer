from newsapi import NewsApiClient
import json
import csv



class News:

  def __init__(self, newsapi=None,bitcoinsNews=None):
    self.newsapi = NewsApiClient(api_key='468dc2b9fc9f4ad08c977058f3623b8a')


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
    data_file = open('data_file.csv', 'w')
    csv_writer = csv.writer(data_file)

    for item in data:
      csv_writer.writerow(item)

    data_file.close()
    


  


