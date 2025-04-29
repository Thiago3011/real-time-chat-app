from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'admin123'
socketio = SocketIO(app)

@app.route('/')
def index():
    return "Servidor iniciado"

if __name__ == '__main__':
    socketio.run(app, debug=True)