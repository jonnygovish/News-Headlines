import urllib.request,json
from .models import News_source

#api key
api_key = None

#base urls
news_source_url = None
article_url = None

def configure_request(app):
  global api_key,news_source_url,article_url
  api_key = app.config['NEWS_API_KEY']
  news_source_url = app.config['NEWS_SOURCE_API_BASE_URL']
  article_url = app.config['NEWS_ARTICLE_BASE_URL']



