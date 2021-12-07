import os
import socket
import redis
from flask import Flask
app = Flask(__name__)

rd = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=os.getenv("REDIS_PORT", "6379"), db=os.getenv("REDIS_DB", "0"))

rd.set("counter", 0)

@app.route('/')
def hello_world():
    counter = rd.incr("counter")
    msg = "Hostname: {}, Counter number: {} ".format(socket.gethostname(), counter)
    return msg
