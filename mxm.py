#!/usr/bin/env python

import os
import sys
import track as TRACK
import artist as ARTIST
import tracking as TRACKING
from Song import *

WANTED_KEYS = {'album_name':'Album', 'track_name':'Track', 'artist_name':'Artist'}
TRACK_KEYS = ['album_name', 'album_id', 'track_name', 'track_id', 'artist_name', 'artist_id', 'lyrics_id', 'album_coverart_100x100']
SONG_KEYS = ['album_name', 'track_name', 'artist_name', 'lyrics']

def makeSong(artist, name):
	songs = searchInfo(artist, name)
	songInfo = getInfo(songs[0])
	song = Song()
	for key in songInfo.keys():
		song.setWhatever(key, songInfo.get(key))
	# print '[*] AFTER SETTING', song
	return song


def searchInfo(artist, name):
	'''
	Search for a song given the artist name and track name.
    Input:  String artist - artist name to search for
            String name   - song name to search for
    Return: List<Track> songs
  	'''
	searchStr = artist + ' ' + name
	songs = TRACK.search(q=searchStr)
	return songs

def getInfo(song, nice=True):
	'''
		Input:	Track song - the song to display the info for
				boolean nice - if true: human readable/minimal
		Output:	dictionary with only useful info
	'''
	tion = song.__dict__
	info = {}
	if nice:
		for key in WANTED_KEYS:
			info[WANTED_KEYS.get(key)] = tion.get(key)
			# print WANTED_KEYS.get(key), '\t:', tion.get(key)
	else:
		for key in TRACK_KEYS:
			info[key] = tion.get(key)
			# print key, '\t\t', tion.get(key)
	# print '[*] SONG INFO >>> ', info
	return info

def showAllInfo(song):
	'''
		Input: Track song - song to display info for
		Output: print all song info to screen
	'''
	tion = song.__dict__
	keys = tion.keys()
	info = {}

	for k in keys:
		info.put(k, tion.get(k))
		# print k, '\t', tion.get(k)
	# print
	return info

if __name__ == "__main__":
	print 'DOING STUFF!!! :)'
	ts = searchTrack('Disturbed', 'Criminal')
	for s in ts:
		# showInfo(s, False)
		showAll(s)

	# for s in ts:
	# 	print str(s)
	# print(ts[0].__dict__)

