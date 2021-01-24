import json
import re
import requests

def format_films(films_response):
  """
  Formats the swapi film response to return an id, title, and release date
  """
  deserialized_response = json.loads(films_response)["results"]
  formatted_response = []
  for film in deserialized_response:
    formatted_response.append(
      {
        "id": extract_id_from_url(film["url"]),
        "title": film["title"],
        "release_date": film["release_date"]
      }
    )
  return json.dumps(formatted_response)

def fetch_and_format_characters(film_response):
  """
  Requests information for individual charcters within a swapi film and
  formats the response to return an id and name for each character
  """
  deserialized_response = json.loads(film_response)["characters"]
  formatted_response = []
  for character in deserialized_response:
    character = json.loads(requests.get(character).text)
    formatted_response.append(
      {
        "id": extract_id_from_url(character["url"]),
        "name": character["name"]
      }
    )
  return json.dumps(formatted_response)

def extract_id_from_url(url):
  """
  The swapi does not include IDs in the JSON response. As a workaround,
  this extracts that value from the provided entity url
  """
  return re.search("/([0-9]+)/", url).group(1)