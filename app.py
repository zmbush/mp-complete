import os
import flask
import logging

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp/'
import sys
import track as TRACK
import artist as ARTIST
import tracking as TRACKING


@app.route('/')
def hello():
  return '<a href="dropbox">Drag and Drop test</a><br /><a href="andre">Andre\'s code</a>'

@app.route('/andre')
def helloAndre():
  tracks = TRACK.search(q='Rick Astley Never Gonna Give You Up')
  for k in range(min(3, len(tracks))):
    print tracks[k]
 #/return "Hello MEEEEE!"
  return str(tracks)

@app.route('/dropbox')
def dropboxPage():
  error = None
  returnVal = flask.render_template('dropbox.html', error=error)
  return returnVal


@app.route('/file_upload', methods=['GET', 'POST'])
def recieveDroppedFile():
  file = flask.request.files['uploaded_file']
  filename = secure_filename(file.filename)
  file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  return file.filename

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  logger = logging.FileHandler('logfiles')
  logger.setLevel(logging.WARNING)
  app.logger.addHandler(logger)
  app.run(host='0.0.0.0', port=port)
