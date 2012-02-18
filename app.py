import os
import flask
import logging
import mxm
import Song

app = flask.Flask(__name__)
import sys


@app.route('/')
def hello():
  return 'Hello World!'

@app.route('/andre')
def helloAndre():
  # tracks = TRACK.search(q='Rick Astley Never Gonna Give You Up')
  # for k in range(min(3, len(tracks))):
  #   print tracks[k]
 #/return "Hello MEEEEE!"
  # return str(tracks)
  song = makeSong('Disturbed', 'Criminal')
  return str(song)


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
