from os import environ
from sufee import app
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000 # 5555
    app.run(HOST, PORT)
