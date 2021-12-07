from flask import Flask
import socket
app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = "My hostname is {} ".format(socket.gethostname())
    return msg
