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
		year (album)
	'''

	def __init__(self):
		pass
	
	data = []
	def __str__(self):
		data[0] = 'Name:\t'
		data[1] = (name + '\n')

		data[2] = 'Artist:\t'
		data[3] = (artist + '\n')

		data[4] = 'Album:\t'
		data[5] = (album + '\n')

		data[6] = 'Year:\t'
		data[7] = (year + '\n')

		data[8] = 'Art:\t'
		data[9] = (art + '\n')

		data[10] = 'Lyrics:\n'
		data[11] = (lyrics + '\n')

	'''SETTERS'''
	def setWhatever(self, key, value):
		if key == 'album_name':
			setAlbum(value)
		elif key == 'artist_name':
			setArtist(value)
		elif key == 'track_name':
			setName(value)
		elif key == 'lyrics':
			setLyrics(value)
		elif key == 'album_coverart_100x100':
			setArt(value)
		else:
			#DONT KNOW WHAT TO DO

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
	def getName():
		self.name = name
	def getArtist():
			self.artist = artist
	def getAlbum():
			self.album = album
	def getLyrics():
			self.lyrics= lyrics
	def getArt():
			self.art = art
	def getYear():
			self.year = year
