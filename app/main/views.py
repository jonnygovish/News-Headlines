from flask import render_template
from . import main

#views
@main.route('/')
def index():
  """
  view root page function that returns the index page and its data
  """
  title = 'News Headlines'
  return render_template('index.html', title = title)