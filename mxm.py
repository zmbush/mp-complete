#!/usr/bin/env python

import os
import sys
import track as TRACK
import artist as ARTIST
import tracking as TRACKING
from Song import Song
from lyrics import findLyrics


# WANTED_KEYS = {'album_name':'Album', 'track_name':'Track', 'artist_name':'Artist'}

ALBUM_NAME = 'album_name'
ALBUM_ID = 'album_id'
TRACK_ID = 'track_id'
TRACK_NAME = 'track_name'
ARTIST_NAME = 'artist_name'
ARTIST_ID = 'artist_id'
LYRICS_ID = 'lyrics_id'
ALBUM_ART = 'album_coverart_100x100'

FIRST = 0

TRACK_KEYS = [ALBUM_NAME, ALBUM_ID, TRACK_NAME, TRACK_ID, ARTIST_NAME, ARTIST_ID, LYRICS_ID, ALBUM_ART]

SONG_KEYS = [ALBUM_NAME, TRACK_NAME, ARTIST_NAME, LYRICS_ID, ALBUM_ART]

def makeSong(artist, name):
	'''
	Call 'searchQuery
			getInfo
		and setWhatever
	'''
	songs = searchQuery(artist, name)
	if len(songs) < 1:
		return None
	songInfo = getInfo(songs[FIRST])
	song = Song()
	for key in songInfo.keys():
		song.setWhatever(key, songInfo.get(key))
	# print '[*] AFTER SETTING', song
	return song

def IDSong(echoID):
	print '[*] >>> ID:', echoID

	try:
		track = TRACK.Track(echoID, echonest=True)
	except Exception as e:
		print "[*] >>> SONG NOT FOUND :("
		print '[*] >>> e:', e
		return None
	songInfo = getInfo(track)
	song = Song()
	for key in songInfo.keys():
		song.setWhatever(key, songInfo.get(key))
	# print '[*] AFTER SETTING', song
	return song	


def searchQuery(artist, name):
	'''
	Search for a song given the artist name and track name.
    Input:  String artist - artist name to search for
            String name   - song name to search for
    Return: List<Track> songs
  	'''
	searchStr = artist + ' ' + name
	songs = TRACK.search(q=searchStr)
	return songs

def getInfo(song):
	'''
		Input:	Track song - the Track to display the info for
		Output:	dictionary with only useful info
	'''
	data = song.__dict__
	info = {}
	for key in SONG_KEYS:
		# if key == 'lyrics_id':
			# info[key] = song.lyrics()
			# break;
		info[key] = data.get(key)
		# print key, '\t\t', data.get(key)
	# print '[*] SONG INFO >>> ', info
	setLyrics(info)

	return info

def rmParends(info):
	name = info[track_name]
	cleanName = []
	flag = True
	for c in name:
		if c == '(':
			flag = False
		elif c == ')':
			flag = True
		elif flag:
			cleanName.append(c)
	return ''.join(cleanName)

def setLyrics(info):
	artist = info[ARTIST_NAME]
	name = info[TRACK_NAME]
	lyrics = findLyrics(artist, name)
	info[LYRICS_ID] = lyrics

def getLyrics(track):
	return track.lyrics()

def showAllInfo(song):
	'''
		Input: Track song - song to display info for
		Output: print all song info to screen
	'''
	tion = song.__dict__
	keys = tion.keys()
	info = {}

	for k in keys:
		info[k] = tion.get(k)
		# print k, '\t', tion.get(k)
	# print
	return info

def showKeys(song):
	for key in song.__dict__:
		print key


if __name__ == "__main__":
	print 'DOING STUFF!!! :)'
	ts = searchQuery('Disturbed', 'Criminal')
	# for s in ts:
	# 	# showInfo(s, False)
	# 	showAll(s)

	# for s in ts:
	# 	print str(s)
	print(ts[0])	

"""
NOTES


{'track_length'				: 256,
'album_name'				: u'Indestructible',
'album_coverart_350x350'	: u'',
'track_mbid'				: u'167e0e87-4631-4c34-bec4-5ce8d6e2b7c7',
'album_id'					: 13944839,
'track_name'				: u'Criminal',
'album_coverart_100x100'	: u'http://api.musixmatch.com/images/albums/9/6/4/1/9/6/11691469.jpg',
'artist_name'				: u'Disturbed',
'track_id'					: 16262847,
'instrumental'				: 0,
'lyrics_id'					: 2848843,
'subtitle_id'				: 0,
'artist_mbid'				: u'4bb4e4e4-5f66-4509-98af-62dbb90c45c5',
'track_rating'				: 100,
'album_coverart_500x500'	: u'',
'artist_id'					: 142,
'album_coverart_800x800'	: u''}

"""