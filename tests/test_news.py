import unittest
from app.models import Movie, News

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1234,'POLITICAL NEWS','US PRESIDENCY','/khsjha27hbs','08/10/2021')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

        # urlToImage, title,description,url, publishedAt