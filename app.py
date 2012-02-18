import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello World!'

@app.route('/andre')
def helloAndre():
  return "Hello Andre!"

@app.route('/dropbox')
def dropboxPage():
  retval = "<html>"
  retval += "</html>"
  return retval

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)