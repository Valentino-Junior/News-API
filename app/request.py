from app import app
import urllib.request,json
from .models import News,Sources
# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]
def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            # print(news_results_list)
            news_results = process_results(news_results_list)
    return news_results
def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        title = news_item.get('title')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        content = news_item.get('content')
        publishedAt = news_item.get('publishedAt')
        news_object = News(title,description,urlToImage,content,publishedAt)
        #print(news_object)
        news_results.append(news_object)
        # print(news_results)
    return news_results