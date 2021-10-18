import flask
from flask import request

app = flask.Flask(__name__, static_folder='/')


@app.route('/')
def index():
    return flask.redirect('static/index.html')


@app.route('/submit', methods=['POST'])
def on_submit():
    name = request.form['name']
    surname = request.form['surname']
    age = request.form['age']
    phone = request.form['phone']
    return f'{name} {surname} {age} {phone}'


if __name__ == '__main__':
    app.run()
