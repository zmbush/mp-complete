#!/usr/bin/env python

import os
import sys
import track as TRACK
import artist as ARTIST
import tracking as TRACKING

WANTED_KEYS = {'album_name':'album_id', 'track_name':'Track', 'artist_name':'Artist'}

TRACK_KEYS = ['album_name', 'album_id', 'track_name', 'track_id', 'artist_name', 'artist_id', 'lyrics_id', 'album_coverart_800x800']

def searchTrack(artist, name):
	searchStr = artist + ' ' + name
	songs = TRACK.search(q=searchStr)
	return songs

"""
album_name
album_id
track_name
track_id
artist_name
artist_id
lyrics_id
album_coverart_800x800
"""

def printNice(song):
	tion = song.__dict__
	for key in WANTED_KEYS:
		print key, '\t:', tion.get(key)

def seeAllKeys(song):
	tion = song.__dict__
	keys = tion.keys()
	for k in keys:
		print k

if __name__ == "__main__":
	print 'DOING STUFF!!! :)'
	ts = searchTrack('Disturbed', 'Criminal')
	printNice(ts[0])

	# for s in ts:
	# 	print str(s)
	# print(ts[0].__dict__)

