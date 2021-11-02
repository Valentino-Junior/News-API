from flask import render_template
from app import app
from .request import get_news
# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    news = get_news()
    title = 'KIMNEWS'
    return render_template('index.html', title = title,articles = news)
