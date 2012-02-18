import urllib
import urllib2
import bs.BeautifulSoup
import json


def findLyrics(artist, song):
	xml = getXML(artist, song)
	lwURL = findURL(xml)
	lyrics = isoLyrics(lwURL)

	return "No lyrics found :(" if (lyrics==None) else lyrics


begtag = '<!-- start of lyrics -->'
endtag = '<!-- end of lyrics -->'


def getXML(artist, song):
	lwurl = makeURL1(artist, song)
	# count = 5
	xml = urllib.urlopen(lwurl)
	xml = xml.read()
	return xml

def makeURL1(artist, song):
	lwurl = 'http://lyrics.wikia.com/api.php?artist=' + srchStr(artist) + '&song=' + srchStr(song) + '&fmt=xml'
	return lwurl


def srchStr(lit):
	'''
	replace spaces with +
	alnum only
	'''
	lit = lit.split()
	new = []
	for l in lit:
		new.append(alnumOnly(l))
	return '+'.join(new)

def alnumOnly(song):
	name = []
	for c in song:
		if c.isalnum():
			name.append(c)
	return ''.join(name)

def findURL(xml):
	soup = BeautifulSoup.BeautifulSoup(xml)
	u = soup.find('url').contents
	u = u[0]
	return u

def makeURL2(url):
	# print url
	return "http://lyrics.wikia.com/api.php?format=json&action=query&prop=revisions&rvprop=content&titles=" + (url.split('/')[-1].replace("_", "%20"))
	
beg = '<lyrics>'
end = '</lyrics>'
def isoLyrics(url):
	new = makeURL2(url)
	print new
	j = urllib2.urlopen(new).read()
	j = json.loads(j)
	j = j["query"]["pages"]
	j = j.itervalues().next()
	try:
		j = j["revisions"][0]['*']
	except:
		return None
	startI = j.find(beg)
	endI = j.find(end)
	lyrics = j[startI+len(beg):endI]
	lyrics = lyrics.strip('\n \t\r')

	return lyrics


	# return htly

# def isoLyrics(html):
# 	startI = html.find(begtag)
# 	endI = html.find(endtag)
# 	htly = html[startI+len(begtag):endI]
# 	# print '[*] >>> BEG:', startI, ' END:',  endI
# 	return htly

# def unHTMLize(htly):
# 	lyrics = []
# 	flag = True
# 	for c in htly:
# 		if c == '<':
# 			flag = False
# 		elif c == '>':
# 			flag = True
# 		elif flag:
# 			lyrics.append(c)
# 	return ''.join(lyrics)

if __name__ == '__main__':
	xml = getXML('ingrid michaelson', 'you and i')
	lwURL = findURL(xml)
	isoLyrics(lwURL)
	# print lwURL
	# html = urllib.urlopen(lwURL)
	# html = html.read()

	# print html

	# htly = isoLyrics(html)
	# lyrics = unHTMLize(htly)
	# print lyrics