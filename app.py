import os
import flask
import logging
import werkzeug
import urllib2
import urllib
import subprocess
from mxm import *
from Song import *
from echonest import track

app = flask.Flask(__name__)
app.debug = True
flask.use_debugger = True
app.config['UPLOAD_FOLDER'] = '/tmp/'
import sys


@app.route('/')
def hello():
  return '<a href="dropbox">Drag and Drop test</a><br /><a href="andre">Andre\'s code</a>'

@app.route('/andre')
def helloAndre():
  # tracks = TRACK.search(q='Rick Astley Never Gonna Give You Up')
  # for k in range(min(3, len(tracks))):
  #   print tracks[k]
  #/return "Hello MEEEEE!"
  # return str(tracks)
  song = makeSong('Shinedown', 'Devour(Album Version)')
  if song != None:
    return str(song).replace('\n', '<br />')
  return ":("


@app.route('/dropbox')
def dropboxPage():
  error = None
  returnVal = flask.render_template('dropbox.html', error=error)
  return returnVal


@app.route('/file_upload', methods=['GET', 'POST'])
def recieveDroppedFile():
  file = flask.request.files['uploaded_file']
  filename = werkzeug.secure_filename(file.filename) 
  path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
  print path
  file.save(path)
  flask.redirect(flask.url_for('uploaded_file', filename=filename))
  newTrack = track.track_from_filename(path)
  # return newTrack.id
  retval = [newTrack.artist, newTrack.title]
  return ','.join(retval)

@app.route('/bridge/<artist>/<song>')
def bridgeTheGap(artist, song):
  print "Artist: " + artist
  print "Song: " + song
  song = makeSong(artist, song)
  return str(song).replace("\n", "<br />")

@app.route('/echo_id/<id>')
def bridgeEchoId(id):
  song = IDSong(echoID = id)
  return song.htmlStr()

@app.route('/uploads/<filename>')
def uploaded_file(filename):
  return flask.send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  logger = logging.FileHandler('logfiles')
  logger.setLevel(logging.WARNING)
  app.logger.addHandler(logger)
  app.run(host='0.0.0.0', port=port)
