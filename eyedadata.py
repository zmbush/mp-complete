from eyeD3 import *
import eyeD3.tag as TAG
	
# FILENAME = "Z:\\Andre Crabb\\Music\\iTunes\\iTunes Music\\Paper Tongues\\Ride To California\\01 Ride To California.mp3"

def updateFile(filename, song):
	tag = eyeD3.Tag()
	tag.link(filename)
	updateLyrics(tag, song.getLyrics())

def updateLyrics(tag, lys):
	tag.addLyrics(lys)
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



