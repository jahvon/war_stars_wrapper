import json
import pytest
import requests_mock

from helper import format_films, fetch_and_format_characters

def test_format_films():
    deserialized_input = {
      "results": [
        {
          "url": "https://swapi.dev/api/films/100/",
          "title": "Star Wars Film X",
          "release_date": "01/01/2021",
          "other_key_z": "random_value"
        },
        {
          "url": "https://swapi.dev/api/films/999/",
          "title": "Wars of Stars",
          "release_date": "01/01/2000",
          "other_key_y": "random_value"
        }
      ],
      "other_key_c": 000,
    }
    serialized_input = json.dumps(deserialized_input)

    expected_output = [
      {
        "id": "100",
        "title": "Star Wars Film X",
        "release_date": "01/01/2021"
      },
      {
        "id": "999",
        "title": "Wars of Stars",
        "release_date": "01/01/2000"
      }
    ]

    response = format_films(serialized_input)
    assert json.dumps(expected_output) == response

def test_characters(requests_mock):
    deserialized_input = {
      "title": "Some Star Wars Movie",
      "characters": [
        "https://swapi.dev/api/people/50/",
        "https://swapi.dev/api/people/75/"
      ],
      "other_key_xyz": "other_value_xyz",
    }
    serialized_input = json.dumps(deserialized_input)
    character_a_response = json.dumps(
      {
        "url": "https://swapi.dev/api/people/50/",
        "name": "Jahvon Dockery",
        "other_key_123": "other_value_123"
      }
    )
    character_b_response = json.dumps(
      {
        "url": "https://swapi.dev/api/people/75/",
        "name": "Loki Poki",
        "other_key_123": "other_value_123"
      }
    )

    # Mock out external methods to isolate unit test's scope
    requests_mock.get("https://swapi.dev/api/people/50/", text=character_a_response)
    requests_mock.get("https://swapi.dev/api/people/75/", text=character_b_response)

    expected_output = [
      {
        "id": "50",
        "name": "Jahvon Dockery"
      },
      {
        "id": "75",
        "name": "Loki Poki"
      }
    ]

    response = fetch_and_format_characters(serialized_input)
    assert json.dumps(expected_output) == response