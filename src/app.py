"""demo application to process csv data"""

import flask

app = flask.Flask(__name__)

@app.route('/')
def welcome_message() -> str:
    return "<h1>Hello, User\nThis is a Demo Flask application</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0')

