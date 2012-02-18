import os
import flask
import logging
import werkzeug
import urllib2
import urllib
from mxm import *
from Song import *

app = flask.Flask(__name__)
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
  song = makeSong('Disturbed', 'Criminal')
  return str(song).replace('\n', '<br />')


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
  API_KEY = 'PQU43GTTUDQXJ4VGA'
  url = 'http://developer.echonest.com/api/v4/track/upload'
  values = {'api_key' : API_KEY,
          'url' : 'http://mp-complete.herokuapp.com/uploads' + filename }
  data = urllib.urlencode(values)
  page = urllib2.urlopen(url, data)
  return page.read()
  return '/uploads/' + filename


@app.route('/uploads/<filename>')
def uploaded_file(filename):
  return flask.send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  logger = logging.FileHandler('logfiles')
  logger.setLevel(logging.WARNING)
  app.logger.addHandler(logger)
  app.run(host='0.0.0.0', port=port)
