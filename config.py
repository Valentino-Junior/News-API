import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&apiKey=8bb8f6be90734a8bbffa24c3e313f257'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
    

