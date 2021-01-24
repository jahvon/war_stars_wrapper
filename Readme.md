# Simple Flask Application

This application is a very simple app that wraps a few [swapi](https://swapi.dev)
api endpoints to return data about Star Wars films.

## Usage

This application can be run from a docker container. First build the docker container
with `docker build . -t warstars`. Afterwards, you can run the docker container
with `docker run -p 8080:8080 warstars`. That docker run command is publishing the 8080
port so the application can be opened locally at http://0.0.0.0:8080.

The only route defined are `/films` and `/characters/<film_id>`.