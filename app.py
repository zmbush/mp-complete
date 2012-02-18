import os
import flask
import logging

app = flask.Flask(__name__)

@app.route('/')
def hello():
  return 'Hello World!'

@app.route('/andre')
def helloAndre():
  return "Hello MEEEEE!"

@app.route('/dropbox')
def dropboxPage():
  print "boo"
  returnVal = flask.render_template('dropbox.html', error=error)


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  logger = logging.FileHandler('logfiles')
  logger.setLevel(logging.WARNING)
  app.logger.addHandler(logger)
  app.run(host='0.0.0.0', port=port)
