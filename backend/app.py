from flask import Flask, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
from login import email_username, email_password

from plants import Plants
from courses import KentCoreCourses, MajorCourses

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Email Form Handler
app.config['MAIL_SERVER']='smtp.mail.yahoo.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = email_username
app.config['MAIL_PASSWORD'] = email_password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
  msg = Message('Hello from the other side!', sender =   'dstephan316@yahoo.com', recipients = ['dstepha3@kent.edu'])
  msg.body = "Hey Daniel, sending you this email from my Flask app, lmk if it works"
  mail.send(msg)
  return "Message sent!"

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