from flask import Flask, jsonify
from flask_socketio import SocketIO
from repository.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'

db.init_app(app)
socketio = SocketIO(app)


@app.route('/initial', methods=['GET'])
def initial_route():
    return jsonify({'message': 'Initial route'})


if __name__ == '__main__':
    socketio.run(app)
