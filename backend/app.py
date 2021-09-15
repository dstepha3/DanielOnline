from flask import Flask, jsonify
from flask_cors import CORS

Plants = [
    {
        'name': 'Pothos',
        'img_src': '@/assets/images/plants/pothos1.jpeg',
    },
    {
        'name': 'Sanseveria',
        'img_src': '@/assets/images/plants/sansevieria.jpg',
    },
    {
        'name': 'Pothos',
        'img_src': '@/assets/images/plants/pothos1.jpeg',
    },
    {
        'name': 'Sanseveria',
        'img_src': '@/assets/images/plants/sansevieria.jpg',
    },
    {
        'name': 'Pothos',
        'img_src': '@/assets/images/plants/pothos1.jpeg',
    }
]

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

@app.route('/api/plants', methods=['GET'])
def my_plants():
    return jsonify(Plants)

if __name__ == '__main__':
    app.run()