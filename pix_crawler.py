#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

from img import imageSave
from file import nameFiles, deleteFiles

# Check the format of the input
# Do premanipulations if necessary
def checkUrl(url):
	# Check if input is null
	if ( input_notation == "" ):
		return default_url
	return url

# Anaylize the url contents
def anaylizeUrl(info, url):
	# Path and number
	path = info['path']
	flag = info['number']
	# Image handler
	imageSave(path, flag, url)

# Create a directory
def createDir(path):
	# Target path exists or not, if not exists then create one
	if os.path.exists( path ) is True:
		print "Path < ", os.path.abspath( path ), " > already existed !!!"
		# Check if it is an empty folder
		if not os.listdir( path ):
			# Empty folder
			print "This file is empty......"
			return {'path' : path, "number" : 0}
		else:
			# Not Empty folder
			print "This file has files......"
			# Wait for next operation to path
			while (1):
				next_handler = raw_input("Override or Following (Please enter O/F) ?")
				if ( next_handler.lower() == 'o' ):
					# Delete existing files in this directory
					deleteFiles( path )
					return {'path' : path, "number" : 0}
					break;
				elif ( next_handler.lower() == 'f' ):
					# Traverse all of the files and keep following
					name_list = nameFiles( path )
					print name_list
					print "The last number of the list is : ", max(name_list)
					return {'path' : path, "number" : max(name_list)+1}
					break;
				else:
					print "Error, you should choose one operation to go!"
	else:
		file = os.mkdir( path )
		return {'path' : path, "number" : 0}

# Entry for the program
if __name__ == '__main__':

	# Designate the path for saving
	save_path_info = createDir('Pix')

	# Default url for test
	default_url = "http://www.ivsky.com/tupian/ziranfengguang/"

	# User input
	input_notation = raw_input( "Enter the key words you want to search : " );
	print "Key words is: ", input_notation

	# Check url legitimacy
	url = checkUrl( input_notation )
	
	# Analyze url contents
	anaylizeUrl( save_path_info, url )
