

from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'your_secret_key'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
