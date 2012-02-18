from mutagen.mp3 import MP3

FILENAME = "Z:\\Andre Crabb\\Music\\iTunes\\iTunes Music\\Sick Puppies\\Tri-Polar\\04 You're Going Down.mp3"

def printData(filename):
	audio = MP3(filename)
	audio.pprint()
	for x in audio.info.dict():
		print x
	# print audio.info
	# print audio.info.length, audio.info.bitrate


if __name__ == "__main__":
	printData(FILENAME)