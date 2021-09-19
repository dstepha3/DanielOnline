from flask import Flask, jsonify
from flask_cors import CORS

from plants import Plants
from courses import KentCoreCourses, MajorCourses

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


#########     Plant Routes      #########
@app.route('/api/plants', methods=['GET'])
def my_plants():
    return jsonify(Plants)


#########      Course Routes      #########
@app.route('/api/courses/kentcore', methods=['GET'])
def kentCore():
    return jsonify(KentCoreCourses)


@app.route('/api/courses/majorcourses', methods=['GET'])
def majorCourses():
    return jsonify(MajorCourses)


#########      Start Flask      #########
if __name__ == '__main__':
    app.run()