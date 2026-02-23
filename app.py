from flask import Flask, render_template
from flask_socketio import SocketIO
from worker import run_scan
import threading

app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def home():
    return render_template("dashboard.html")

@socketio.on("start_scan")
def start_scan(data):

    target = data["target"]

    thread = threading.Thread(
        target=run_scan,
        args=(socketio, target)
    )
    thread.start()

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
