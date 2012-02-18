import urllib2

def findLyrics(artist, song):
	html = getHTML(artist, song)
	htly = isoLyrics(html)
	lyrics = unHTMLize(htly)
	return lyrics

begtag = '<!-- start of lyrics -->'
endtag = '<!-- end of lyrics -->'

def getHTML(artist, song):
	azurl = makeURL(artist, song)
	html = urllib2.urlopen(azurl)
	html = html.read()
	return html


def makeURL(artist, song):
	azurl = 'http://www.azlyrics.com/lyrics/' + alnumOnly(artist.lower()) + '/' + alnumOnly(song.lower()) + '.html'
	# print '[*] >>> URL=', azurl
	return azurl

def alnumOnly(song):
	name = []
	for c in song:
		if c.isalnum():
			name.append(c)
	return ''.join(name)

def isoLyrics(html):
	startI = html.find(begtag)
	endI = html.find(endtag)
	htly = html[startI+len(begtag):endI]
	# print '[*] >>> BEG:', startI, ' END:',  endI
	return htly

def unHTMLize(htly):
	lyrics = []
	flag = True
	for c in htly:
		if c == '<':
			flag = False
		elif c == '>':
			flag = True
		elif flag:
			lyrics.append(c)
	return ''.join(lyrics)

if __name__ == '__main__':
	html = getHTML('My Chemical Romance', 'Welcome To The Black Parade')
	htly = isoLyrics(html)
	lyrics = unHTMLize(htly)
	print lyrics