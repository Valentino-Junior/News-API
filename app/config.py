class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
class ProdConfig(Config):
    '''
    Child class for production setup
    Args:
        Config: General configuration options are found in the parent configuration class.
        
    '''
    pass
class DevConfig(Config):
    '''
    Child class for production setup
    
    Args:
        Config: General configuration options are found in the parent configuration class.
        
    '''
    DEBUG = True

