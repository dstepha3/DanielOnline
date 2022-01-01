
from flask import Flask, jsonify
from flask_cors import CORS     # type: ignore


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


from api import *


if __name__ == '__main__':
    app.run() 