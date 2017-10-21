import os

class Config:
  NEWS_SOURCE_API_BASE_URL = 'https://newsapi.org/v1/sources?category={}&language=en'
  # NEWS_SOURCE_API_BASE_URL = 'https://newsapi.org/v1/sources?'
  NEWS_ARTICLE_BASE_URL ='https://newsapi.org/v1/articles?source={}&sortBy=latest&apiKey={}'
  NEWS_API_KEY= os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True


config_options = {
  'development': DevConfig,
  'production': ProdConfig
}