import os
import flask
import logging

app = flask.Flask(__name__)
import sys
import track as TRACK
import artist as ARTIST
import tracking as TRACKING


@app.route('/')
def hello():
  return 'Hello World!'

@app.route('/andre')
def helloAndre():
  tracks = TRACK.search(q="Distured In The Fire")
  for k in range(min(3, len(tracks))):
    print tracks[k]
 #/return "Hello MEEEEE!"
  return str(tracks)

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
