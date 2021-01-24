import requests

from cachetools import TTLCache
from flask import Flask
from helper import fetch_and_format_characters, format_films

app = Flask(__name__)
cache = TTLCache(maxsize=32, ttl=3600)

@app.route('/films')
def films():
  """
  Returns the id, title, and release date of all Star Wars films
  """
  if "all_films" not in cache:
    films_response = requests.get("https://swapi.dev/api/films/")
    cache["all_films"] = format_films(films_response.text)

  return cache["all_films"]

@app.route('/characters/<film_id>')
def characters(film_id):
  """
  Returns the id and name of all of the characters in a given Star Wars film
  """
  cache_key = "characters_for_"+str(film_id)
  if cache_key not in cache:
    film_response = requests.get("https://swapi.dev/api/films/"+str(film_id))
    cache[cache_key] = fetch_and_format_characters(film_response.text)

  return cache[cache_key]