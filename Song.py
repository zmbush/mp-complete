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
		self.name = ' '
		self.artist = ' '
		self.album = ' '
		self.lyrics = ' '
		self.art = ' '
		self.year = ' '
	
	def __str__(self):
		data = []
		data.append('Name:\t')
		data.append((self.name + '\n'))

		data.append('Artist:\t')
		data.append((self.artist + '\n'))

		data.append('Album:\t')
		data.append((self.album + '\n'))

		data.append('Year:\t')
		data.append((self.year + '\n'))

		data.append('Art:\t')
		data.append((self.art + '\n'))

		data.append('Lyrics:\n')
		data.append((self.lyrics + '\n'))

		return ''.join(data)

	'''SETTERS'''
	def setWhatever(self, key, value):
		# print '[*] SETTING ', key, value
		if key == 'Album':
			self.setAlbum(value)
		elif key == 'Artist':
			self.setArtist(value)
		elif key == 'Track':
			self.setName(value)
		elif key == 'Lyrics':
			self.setLyrics(value)
		elif key == 'Art':
			self.setArt(value)
		else:
			#DONT KNOW WHAT TO DO
			print 'NOTHING!!!'

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