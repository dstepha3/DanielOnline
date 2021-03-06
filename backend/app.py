
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS     # type: ignore
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig, ProductionConfig
from hmac import HMAC, compare_digest
from hashlib import sha256
from http import HTTPStatus
from datetime import datetime
import os


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__, template_folder="../../frontend/dist/")
app.config.from_object(__name__)


if os.environ['FLASK_ENV'] == "development":
    app.config.from_object(DevelopmentConfig)
else:
    import git
    app.config.from_object(ProductionConfig)


#initialize database
db = SQLAlchemy(app)

#model
class Users(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    userEmail = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    adminStatus = db.Column(db.Integer, nullable=False, default=0)
    userFirst = db.Column(db.String(200), nullable=False)
    userLast = db.Column(db.String(200), nullable=False)
    #date = db.Column(db.DateTime, default=datetime.utcnow)

    def as_dict(self):
        return { col.name: getattr(self, col.name) for col in self.__table__.columns }
        

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)

if os.environ['FLASK_ENV'] == "production":
    # Initial page rendering needed for PythonAnywhere
    # requires npm run build to be run in /frontend first
    @app.route('/')
    def index():
        try:
            return render_template('index.html')
        except:
            return "There is not currently a /frontend/dist folder for the built frontend files. Type <b>npm run build</b> under /frontend to create it"

    def verify_signature(request):
        try:
            received_signature = request.headers["X-Hub-Signature-256"].split("sha256=")[1]
        except:
            return "Invalid signature", HTTPStatus.BAD_REQUEST

        key_as_bytes = bytes(app.config['SECRET_KEY'], 'utf-8')
        expected_signature = HMAC(
            key=key_as_bytes, msg=request.data, digestmod=sha256).hexdigest()

        return compare_digest(received_signature, expected_signature)

    # require API key for each request on pythonanywhere

    @app.before_request
    def before_request_func():
        if request.endpoint == "index" or request.endpoint == "update_server":
            return
          
        api_key = request.headers["Api-Key"]
        if api_key is None:
            return "API Key is required", HTTPStatus.BAD_REQUEST

        if api_key != app.config['SECRET_KEY']:
            return "Invalid API Key", HTTPStatus.BAD_REQUEST

          
    # for server updates
    @app.route('/update_server', methods=['POST'])
    def update_server():
        if request.method == 'POST':
            if verify_signature(request):
                repo = git.Repo('/home/dstepha3/DanielOnline')
                origin = repo.remotes.origin

                origin.pull()
                return 'Updated PythonAnywhere successfully'
            else:
                return "Incorrect signature", HTTPStatus.FORBIDDEN
        else:
            return 'Wrong event type', HTTPStatus.BAD_REQUEST


from api import *

if __name__ == '__main__':
    app.run() 