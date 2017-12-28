import os
import re
import lxml

from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve

from util.fileutil import *

class VxExtractor:
	def __init__(self, url):
		self.doc = urlopen(url).read()
		self.soup = BeautifulSoup(self.doc, "lxml")
	
	# Save contents to file
	def saveDoc(self):
		file_name = '../raw_data/' + self.soup.title.string + '.txt'
		saveFile(file_name, self.doc)
	
	# All cleaned texts
	def getAllTxts(self):
		text = self.soup.get_text()
		# Split into tokens by white space
		tokens = text.split()
		# remove remaining tokens that are not alphabetic(at least one other character)
		#tokens = [word for word in tokens if word.isalpha()]
		return tokens
	
	# Parse accessed data from URL
	def parseUrl(self, label):
		# Store image URL
		image = []
		# Save target files, http://img.ivsky.com/img/tupian/li/201709/24/yueqiu-002.jpg
		# 1. Save to different folder (img, ...) with related data
		# 2. TimeStamp
		for link in self.soup.find_all(label):
			imgUrl = link.get('src')
			image.append(imgUrl)
		for item in image:
			name = item.split('/')[-1]
			urlretrieve(item, '../data/image/' + name)

if __name__ == '__main__':
	# Default settings for test
	default_label = 'img'
	# default_url = "http://www.ivsky.com/tupian/ziranfengguang/"
	default_url = "http://www.dytt8.net/"
	
	vx = VxExtractor(default_url)
	vx.saveDoc()
	
	print(vx.getAllTxts())