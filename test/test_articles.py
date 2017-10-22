import unittest
from app.models import Articles

class TestArticle(unittest.TestCase):
  '''
	Test Class to test the behaviour of the Article class
	'''
  def setUp(self):
    '''
    Set up that will run before every Test
    '''
    self.new_article = Articles("Angela Medina","Redesigning the TechCrunch app","Over the last two years we have been working hard to improve the experience of TechCrunch products for our readers","https://techcrunch.com/2017/10/21/redesigning-the-techcrunch-app/","https://tctechcrunch2011.files.wordpress.com/2017/10/1-lead-image.jpg","2017-10-21T11:00:53Z")

  def test_instance(self):
    self.assertTrue(isinstance(self.new_article,Articles))
		
if __name__ == '__main__':
	unittest.main(verbosity=2)