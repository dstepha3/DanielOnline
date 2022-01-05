
from flask import jsonify
from app import app, db, Users

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/api/user/', methods=['GET'])
def get_user():
    user = db.session.query(Users).all()

    arr_user = []
    for the_user in user:
        arr_user.append(the_user.as_dict())

    return jsonify(user_info = arr_user)
