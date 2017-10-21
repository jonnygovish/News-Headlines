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

def get_source(category):
  """
  """
  get_source_url = news_source_url.format(category)

  with urllib.request.urlopen(get_source_url) as url:
    get_source_data = url.read()
    get_source_response = json.loads(get_source_data)

    source_results = None

    if get_source_response['sources']:
      source_result_list =get_source_response['sources']

      source_results = process_results(source_result_list)
  
  return source_results

def process_results(source_list):
  """
  """
  source_results = []

  for source_item in source_list:
    id = source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')
    url = source_item.get('url')
    category = source_item.get('category')

    source_object = News_source(id,name,description,url,category)
    source_results.append(source_object)

  return source_results

  



