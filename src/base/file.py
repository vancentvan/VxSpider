#!/usr/bin/env python

import os
import codecs

# Create directory for target path
def createDir(dir):
	if not os.path.exists(dir):
		os.mkdir(dir)

# Delete files under target directory
def emptyDir(dir):
	for file in os.listdir(dir):
		del_file = os.path.join(dir, file)
		if os.path.isfile(del_file):
			os.remove(del_file)

# Save data to file
def saveFile(dir, fn, data):
	createDir(dir)
	#print(type(data))
	file = "%s/%s" % (dir, fn)
	if type(data).__name__ == 'str':
		print('String')
		with codecs.open(file, 'w', 'utf-8') as f:
			f.write(data)
	if type(data).__name__ == 'bytes':
		with codecs.open(file, 'wb') as f:
			f.write(data)