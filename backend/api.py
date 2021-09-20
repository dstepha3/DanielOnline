
from flask import jsonify
from app import app

from plants import Plants
from courses import KentCoreCourses, MajorCourses

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
