from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'admin123'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print(f"Mensagem {message} recebida")
    send(f"Thiago: {message}")

if __name__ == '__main__':
    socketio.run(app, debug=True)