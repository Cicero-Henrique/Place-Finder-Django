# Place Finder

This project allows you to find places in any city around the world using Yelp Api.

# Usage

First, you will need to create a .txt file in the root folder called 'SECRET_KEY'.
The first line must contain your Client ID of YELP and the second line your API Key.

```
    pip install -r requirements.txt
    python manage.py runserver
```

# Docker

In the root folder, you can run:

```
    docker build -t "Your image name" .
    docker run -p 8000:8000 "Your image name"
```

Or using Docker Compose:
```
    docker-compose -f "docker-compose.yaml"  build
    docker-compose up
```

# Requirements

* [Yelp Keys](https://www.yelp.com/developers/v3/manage_app)
* [Python 3.7+](https://www.python.org/downloads/)
* [Python pip](https://pip.pypa.io/en/stable/installing/)
* [Docker](https://www.docker.com/products/docker-desktop)