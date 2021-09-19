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
        'name': 'Algaonema',
        'img_src': 'https://i.imgur.com/VYlR2xC.jpg', 
        'modal_id': '#aglaModal',
        'active': False,
    },
    {
        'name': 'Dracaena',
        'img_src': 'https://i.imgur.com/BAAcnBa.jpg', 
        'modal_id': '#dracaenaModal',
        'active': False,
    },
    {
        'name': 'Epipremnum',
        'img_src': 'https://i.imgur.com/GkMG42V.jpg', 
        'modal_id': '#epipremnumModal',
        'active': False,
    },  
    {
        'name': 'Ficus',
        'img_src': 'https://i.imgur.com/UlpMVYC.jpg', 
        'modal_id': '#ficusModal',
        'active': False,
    },
    {
        'name': 'Garden',
        'img_src': 'https://i.imgur.com/SQHHpAh.jpg', 
        'modal_id': '#gardenModal',
        'active': False,
    },
    {
        'name': 'Miscellaneous',
        'img_src': 'https://i.imgur.com/QGAckPl.jpg', 
        'modal_id': '#miscModal',
        'active': False,
    },  
    {
        'name': 'Palms',
        'img_src': 'https://i.imgur.com/g6K5yWX.jpg', 
        'modal_id': '#palmsModal',
        'active': False,
    }, 
    {
        'name': 'Philodenderon',
        'img_src': 'https://i.imgur.com/oibHCCL.jpg', 
        'modal_id': '#philoModal',
        'active': False,
    },
    {
        'name': 'Rhapidophora',
        'img_src': 'https://i.imgur.com/xgipV3i.jpg', 
        'modal_id': '#rhaphModal',
        'active': False,
    },
    {
        'name': 'Sanseveria',
        'img_src': 'https://i.imgur.com/mFNFLKQ.jpg', 
        'modal_id': '#snakeModal',
        'active': False,
    },
    {
        'name': 'Scindapsus',
        'img_src': 'https://i.imgur.com/M9cuNAp.jpg', 
        'modal_id': '#scindapsusModal',
        'active': False,
    },
    {
        'name': 'Succulents',
        'img_src': 'https://i.imgur.com/ZUJ6z6A.jpg', 
        'modal_id': '#succulentsModal',
        'active': False,
    },
    {
        'name': 'Syngonium',
        'img_src': 'https://i.imgur.com/3EIGCWD.jpg', 
        'modal_id': '#syngoniumModal',
        'active': False,
    },
    {
        'name': 'ZZ',
        'img_src': 'https://i.imgur.com/Z1j8zPC.jpg', 
        'modal_id': '#zzModal',
        'active': False,
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