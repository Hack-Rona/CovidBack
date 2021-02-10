from flask import Flask, jsonify, g

import models
from resources.volunteers import volunteer
from resources.gethelps import gethelp
DEBUG = True
PORT = 8000

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

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

# The default URL ends in / ("my-website.com/").
@app.route('/')
def index():
    return 'hi'

# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
