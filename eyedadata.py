from eyeD3 import *
import eyeD3.tag as TAG
	
# FILENAME = "Z:\\Andre Crabb\\Music\\iTunes\\iTunes Music\\Paper Tongues\\Ride To California\\01 Ride To California.mp3"

def updateFile(filename, song):
	tag = eyeD3.Tag()
	try:
		tag.link(filename)
		updateLyrics(tag, song.getLyrics())
		updateName(tag, song.getName())
		updateArtist(tag, song.getArtist())
		updateAlbum(tag, song.getAlbum())
	except TypeError as e:
		return e
		print '[*] >>> TypeError', e
		return False
	except eyeD3.tag.TagException as f:
		return f
		print '[*] >>> TagException', f
		return False

def updateLyrics(tag, lys):
	tag.addLyrics(lys)
	tag.update()
	return True
def updateName(tag, name):
	tag.setTitle(name)
	tag.update()
	return True
def updateArtist(tag, artist):
	tag.setArtist(artist)
	tag.update()
	return True
def updateAlbum(tag, album):
	tag.setAlbum(album)
	tag.update()
	return True




if __name__ == "__main__":
	f = FILENAME
	print f

	tag = eyeD3.Tag()
	tag.link(f)

	print tag.getArtist()
	print tag.getAlbum()
	print tag.getTitle()

	tag.addLyrics("hello!!!")
	tag.update()

	lFrames = tag.getLyrics()
	for l in lFrames:
		print l.lyrics
	# if lFrame != None:
	# 	print lFrame.lyrics



