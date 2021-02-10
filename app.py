from flask import Flask, jsonify, g
from flask_mail import Mail, Message

import models
from resources.volunteers import volunteer
from resources.gethelps import gethelp
DEBUG = True
PORT = 8000

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)
mail = Mail(app)

#LLogic for our dtatbase connection
@app.before_request
def before_request():
    """Connect to the database befoe the request"""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """Close db after request"""
    g.db.close()
    return response

app.register_blueprint(volunteer, url_prefix='/volunteers')
app.register_blueprint(gethelp, url_prefix='/gethelps')

# Flask_mail server params
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '1800callcovaid@gmail.com'
app.config['MAIL_PASSWORD'] = 'VaccinateNow!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# The default URL ends in / ("my-website.com/").
@app.route('/')
def index():
    msg = Message('Hello', sender = '1800callcovaid@gmail.com', recipients = ['shane@shanestarkweather.com'])
    msg.body = 'This message is coming to you from the back end of the Covaid app!!'
    mail.send(msg)
    return 'hi'

# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
