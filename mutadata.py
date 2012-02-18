from mutagen.mp3 import MP3
from mutagen.id3 import ID3

FILENAME = "Z:\\Andre Crabb\\Music\\iTunes\\iTunes Music\\Sick Puppies\\Tri-Polar\\04 You're Going Down.mp3"

def printData(filename):
	data = ID3(filename)
	data.pprint()
	# print audio.info.length
	print data.pprint()

	# for x in audio.info.length:
		# print x
	# print audio.info
	# print audio.info.length, audio.info.bitrate


if __name__ == "__main__":
	printData(FILENAME)