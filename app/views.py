from flask import render_template
from app import app
from .request import get_news
# Views
@app.route('/')
def index():
    '''
    The index page and its contents are returned by the View root page function.

    '''
    title = 'F-CLASS NEWS'
    news = get_news()
    return render_template('index.html', title = title,articles = news)
