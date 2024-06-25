from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from repository.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'

db.init_app(app)
socketio = SocketIO(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    emit('message', data, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
