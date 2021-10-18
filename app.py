import flask
from flask import request

app = flask.Flask(__name__, static_folder='/')


registered_phones = []


@app.route('/')
def index():
    return flask.redirect('static/index.html')


@app.route('/submit', methods=['POST'])
def on_submit():
    name = request.form['name']
    surname = request.form['surname']
    age = request.form['age']
    phone = request.form['phone']
    if phone in registered_phones:
        return 'Данный номер уже зарегистрирован!'
    else:
        registered_phones.append(phone)
        return 'Пользователь добавлен в базу!'


if __name__ == '__main__':
    app.run()
