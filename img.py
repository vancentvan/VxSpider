#!/usr/bin/env python
#-*- coding:utf-8 -*-

import lxml, urllib

from bs4 import BeautifulSoup
from urllib2 import urlopen

def imageSave(path, flag, url):
	# Array to store all image paths
	image = []
	# Read all contents in a doc
	doc = urlopen( url ).read()
	soup = BeautifulSoup( doc, "lxml" )
	for child in soup.title:
		print child
	print '\n'
	# Save target files
	for link in soup.find_all( 'img' ):
		print( link.get('src') )
		print "--" * 40
		image.append( link.get('src') ) 
	for item in image:
		urllib.urlretrieve( item, path + '\\%s.jpg' % flag )
		flag += 1
