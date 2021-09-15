from flask import Flask, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#img_src's must be direct links for some reason,
#chose imgur as image host
Plants = [
    {
        'name': 'Pothos',
        'img_src': 'https://i.imgur.com/GkMG42V.jpg', 
        'modal_id': '#epipremnumModal',
    },  
    {
        'name': 'Sanseveria',
        'img_src': 'https://i.imgur.com/OcyBTM4.jpg', 
        'modal_id': '#snakeModal',
    }
]




# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/api/plants', methods=['GET'])
def my_plants():
    return jsonify(Plants)

if __name__ == '__main__':
    app.run()