from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '1800callcovaid@gmail.com'
app.config['MAIL_PASSWORD'] = 'VaccinateNow!'
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_DEFAULT_SENDER'] = '1800callcovaid@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hello', recipients=['shane@shanestarkweather.com'])
    mail.send(msg)
    return 'Message Sent!'

if __name__ == '__main__':
    app.run(debug=True)