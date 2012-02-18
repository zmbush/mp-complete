ALBUM_NAME = 'album_name'
ALBUM_ID = 'album_id'
TRACK_ID = 'track_id'
TRACK_NAME = 'track_name'
ARTIST_NAME = 'artist_name'
ARTIST_ID = 'artist_id'
LYRICS_ID = 'lyrics_id'
ALBUM_ART = 'album_coverart_100x100'

class Song(object):
	'''
	Class to store Song info in a manageable format.
	'''

	'''
		VARS
		=====
		name
		artist
		album
		lyrics
		art
	'''


	def __init__(self):
		self.name = ' '
		self.artist = ' '
		self.album = ' '
		self.lyrics = ' '
		self.art = ' '
		self.year = ' '
	
	def htmlStr(self):
		return str(self).replace('\n', '<br />')

	def __str__(self):
		data = []
		data.append('Name:\t')
		data.append((self.name + '\n'))

		data.append('Artist:\t')
		data.append((self.artist + '\n'))

		data.append('Album:\t')
		data.append((self.album + '\n'))

		data.append('Art:\t')
		data.append((self.art + '\n'))

		data.append('Lyrics:\n')
		data.append(self.lyrics + '\n')

		return ''.join(data)

	'''SETTERS'''
	def setWhatever(self, key, value):
		# print '[*] SETTING ', key, value
		if key == ALBUM_NAME:
			self.setAlbum(value)
		elif key == ARTIST_NAME:
			self.setArtist(value)
		elif key == TRACK_NAME:
			self.setName(value)
		elif key == LYRICS_ID:
			self.setLyrics(value)
		elif key == ALBUM_ART:
			self.setArt(value)
		else:
			#DONT KNOW WHAT TO DO
			print '[*] >>> TRYING TO ADD', key, value

	def setName(self, name):
		'''
		String name
		'''
		self.name = name
	def setArtist(self, artist):
		'''
		String artist
		'''
		self.artist = artist
	def setAlbum(self, album):
		'''
		String album
		'''
		self.album = album
	def setLyrics(self, lyrics):
		'''
		String lyrics
		'''
		self.lyrics= lyrics
	def setArt(self, art):
		'''
		String art
		'''
		self.art = art
	def setYear(self, year):
		'''
		String year
		'''
		self.year = year

	'''GETTERS'''
	def getName(self):
		return self.name
	def getArtist(self):
		return self.artist
	def getAlbum(self):
		return self.album
	def getLyrics(self):
		return self.lyrics
	def getArt(self):
		return self.art
	def getYear(self):
		return self.year