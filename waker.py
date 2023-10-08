from flask import Flask
from threading import Thread

s = Flask(__name__)


@s.route('/')
def ping():
  return "Pong!"


def run():
  s.run(host='0.0.0.0', port=8000)


def server():
  t = Thread(target=run)
  t.start()
