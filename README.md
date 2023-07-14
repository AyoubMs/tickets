python-flask-tickets
========

# Setup
This is a simple ticket-tracking flask application with a JSON API

## Create Python 3.7 virtual environment
```
cd python-flask-tickets
pipenv --python python3.7 install flask python-dotenv psycopg2-binary Flask-SQLAlchemy Flask-Migrate
pipenv shell
mkdir templates static
touch {templates,static}/.gitkeep
vi config.py
vi models.py
vi __init__.py
```
