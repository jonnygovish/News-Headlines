from flask import render_template
from . import main
from ..request import get_source

#views
@main.route('/')
def index():
  """
  view root page function that returns the index page and its data
  """

  business_source = get_source('business')
  entertainment_source = get_source('entertainment')
  general_source = get_source('general')
  gaming_source = get_source('gaming')
  technology_source = get_source('technology')
  politics_source = get_source('politics')
  music_source = get_source('music')
  sport_source = get_source('sport')
  print(sport_source)
  title = 'News Headlines'
  return render_template('index.html', title = title, sport = sport_source,business = business_source, entertainment = entertainment_source, general = general_source, gaming = gaming_source, technology = technology_source, politics = politics_source, music = music_source)