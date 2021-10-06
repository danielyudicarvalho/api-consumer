from api_collect import *
from newsapi import NewsApiClient
import sys



if __name__ == '__main__':
    print('-----------------------------------------')
    print("Bem vindo")
    print('-----------------------------------------')

    print('Escolha a API que deseja consumir')
    print(" 1 - News API (API de notícias)")
    print(" 2 - Aletheia (API de dados financeiros)")
    print(" 3 - Fake API (API de dados aletórios )")

    name_api = input('Escolha a API que deseja consumir')
    print('---------')

    if name_api == "1":
      print("news_api")
      api = Collect("news")
      api.collect()
    elif name_api == "2":
      print("você escolheu Aletheia API")
      api = Collect("aletheia")
      api.collect()
    elif name_api == "3":
      print("você escolheu Fake API")
      api = Collect("fake")
      api.collect()
    elif name_api == "0":
      print("fechando o programa")
      sys.exit()
    else:
      print("escolha inválida")
      
      
      
      
      