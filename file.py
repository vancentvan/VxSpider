#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

# Retrieve names for files in target directory
def nameFiles(dir):
	# Save all the img numbers
	name_num = []
	for file in os.listdir( dir ):
		name_file = file[:-4]
		# Convert string to integer and save into an array
		name_num.append( int(name_file) );
	return name_num

# Delete files under target directory
def deleteFiles(dir):
	for file in os.listdir( dir ):
		del_file = os.path.join( dir, file )
		if os.path.isfile( del_file ):
			os.remove( del_file )
