import pytest
import requests_mock

from main import app
from pytest_mock import mocker

@pytest.fixture
def client():
    return app.test_client()

def test_films(client, requests_mock, mocker):
    # Mock out external methods to isolate unit test's scope
    requests_mock.get("https://swapi.dev/api/films/", text="mocked_films_data")
    expected = "formated_mock_films_data"
    mocker.patch("main.format_films", return_value=expected)

    response = client.get("/films")
    assert response.status_code == 200
    assert expected == response.get_data(as_text=True)

def test_characters(client, requests_mock, mocker):
    # Mock out external methods to isolate unit test's scope
    requests_mock.get("https://swapi.dev/api/films/1", text="mocked_film_data")
    expected = "formated_mock_characters_data"
    mocker.patch("main.fetch_and_format_characters", return_value=expected)

    response = client.get("/characters/1")
    assert response.status_code == 200
    assert expected == response.get_data(as_text=True)