from aletheia import *
from apinews import *
from fakeapi import *


class Collect:
  def __init__(self, api,collector=None):
    self.name = api
    if self.name == 'news':
      self.collector =  News()
    elif self.name == 'aletheia':
      self.collector = Aletheia()
    elif self.name == 'fake':
      self.collector = Fake()

  def collect(self):
    self.collector.collect()


