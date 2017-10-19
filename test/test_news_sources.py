import unittest
from app.models import News_source

class News_sourceTest(unittest.TestCase):
  """
  Test Class to test the behaviour of the News_source class
  """
  def setUp(self):
    """
    Set up tat will run before every Test
    """
    self.new_source =News_source("bbc-sport","BBC SPORT", "The home of BBC Sport online.","http://www.bbc.co.uk/sport","sport")

  # def test_init(self):
    
