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
        'img_src': 'https://i.imgur.com/SMzMYJW.png', 
        'modal_id': '#algaonemaModal',
        'active': False,
    },
    {
        'name': 'Dracena',
        'img_src': 'https://i.imgur.com/SMzMYJW.png', 
        'modal_id': '#dracenaModal',
        'active': False,
    },
    {
        'name': 'Calathea',
        'img_src': 'https://i.imgur.com/SMzMYJW.png', 
        'modal_id': '#calatheaModal',
        'active': False,
    },
    {
        'name': 'Epipremnum',
        'img_src': 'https://i.imgur.com/GkMG42V.jpg', 
        'modal_id': '#epipremnumModal',
        'active': True,
    },  
    {
        'name': 'Ficus',
        'img_src': 'https://i.imgur.com/SMzMYJW.png', 
        'modal_id': '#ficusModal',
        'active': True,
    },
    {
        'name': 'Maranta',
        'img_src': 'https://i.imgur.com/SMzMYJW.png', 
        'modal_id': '#marantaModal',
    },
    {
        'name': 'Miscellaneous',
        'img_src': 'https://i.imgur.com/SMzMYJW.png', 
        'modal_id': '#miscModal',
        'active': True,
    },
    {
        'name': 'Garden',
        'img_src': 'https://i.imgur.com/kmhnJC5.jpg', 
        'modal_id': '#gardenModal',
        'active': True,
    },  
    {
        'name': 'Palms',
        'img_src': 'https://i.imgur.com/g6K5yWX.jpg', 
        'modal_id': '#palmsModal',
        'active': True,
    }, 
    {
        'name': 'Philodenderon',
        'img_src': 'https://i.imgur.com/SMzMYJW.png', 
        'modal_id': '#philoModal',
        'active': True,
    },
    {
        'name': 'Rhapidophora',
        'img_src': 'https://i.imgur.com/SMzMYJW.png', 
        'modal_id': '#rhaphModal',
        'active': True,
    },
    {
        'name': 'Sanseveria',
        'img_src': 'https://i.imgur.com/OcyBTM4.jpg', 
        'modal_id': '#snakeModal',
        'active': True,
    },
    {
        'name': 'Scindapsus',
        'img_src': 'https://i.imgur.com/SMzMYJW.png', 
        'modal_id': '#scindapsusModal',
        'active': True,
    },
    {
        'name': 'Succulents',
        'img_src': 'https://i.imgur.com/ZUJ6z6A.jpg', 
        'modal_id': '#succulentsModal',
        'active': True,
    },
    {
        'name': 'ZZ',
        'img_src': 'https://i.imgur.com/Z1j8zPC.jpg', 
        'modal_id': '#zzModal',
        'active': True,
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