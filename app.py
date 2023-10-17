from logging import debug
from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
  return "<p>Olá mundo</p>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  