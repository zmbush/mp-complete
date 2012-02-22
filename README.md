
.mp-Complete
===========

.mp-Complete is a simple web application to fix the metadata on songs. Simply
drop an mp3 file onto the webpage, and get back the repaired file!

Our Files
---------
### app.py

The main Flask app.


### eyedadata.py

Reads and updates the ID3 data in the MP3 Files
Using: eyeD3


### lyrics.py

Reads lyrics from lyrics.wikia.com
Using BeautifulSoup


### mxm.py

Queries Musixmatch's json library to get information about songs


### Song.py

A class to store data about songs

Libraries Used
--------------

### eyeD3
### BeautifulSoup
### Musixmatch Python API
### EchoNest Python API
