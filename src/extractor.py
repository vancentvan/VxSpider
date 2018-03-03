#!/usr/bin/env python

import os
import re
import lxml

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve

from base.file import *

from model.movie import *
from model.ticket import *

class VxExtractor:
	def __init__(self, user_agent):
		# Do some initialization
		self.user_agent = user_agent
		
	def init(self, url):
		headers = {'User-Agent' : self.user_agent}  
		req = Request(url=url, headers=headers)  		
		self.doc = urlopen(req).read()
		self.soup = BeautifulSoup(self.doc, "lxml")
	
	# Save contents to file
	def saveDoc(self, dir='../raw_data/', suffix='txt'):		
		''' If title contains special signs, then choose the first sentence '''
		title = self.soup.title.string
		if ',' in title:
			title = re.sub('\W+', '', title.split(',')[0])
		fn = "%s.%s" % (title, suffix)
		saveFile(dir, fn, self.doc)
	
	# All cleaned texts
	def getAllTxts(self):
		text = self.soup.get_text()
		# Split into tokens by white space
		tokens = text.split()
		# remove remaining tokens that are not alphabetic(at least one other character)
		#tokens = [word for word in tokens if word.isalpha()]
		return tokens
	
	# Parse image resource
	def parseImg(self, dir='../data/image/'):
		# Create directory
		createDir(dir)
		# Store image URL
		image = []
		# Save target files, http://img.ivsky.com/img/tupian/li/201709/24/yueqiu-002.jpg
		# 1. Save to different folder (img, ...) with related data
		# 2. TimeStamp
		for link in self.soup.find_all('img'):
			imgUrl = link.get('src')
			image.append(imgUrl)
		for item in image:
			name = item.split('/')[-1]
			urlretrieve(item, dir + name)
	
	# Parse information and save
	def parseInfo(self, resource_type, suffix='txt'):
		# Directory and file name
		directory = '../data/info/'
		file_name = "%s_info.%s" % (resource_type, suffix)
		# Parse information
		if (resource_type == 'movie'):
			saveFile(directory, file_name, parseMovieInfo(self.soup))
		if (resource_type == 'ticket'):
			saveFile(directory, file_name, parseTicketInfo(self.soup))
		

if __name__ == '__main__':
	# Default settings for test
	# default_urls = ["http://www.ivsky.com", # Image
	# 				"https://www.technologyreview.com", # News
	# 				"http://www.btapple.com", # Movie
	# 				"https://www.cnbc.com", # Stock
	# 				"http://www.tickethk.com", # Ticket
	# 				"https://www.taobao.com", # TaoBao
	# 				"https://www.jd.com" # JingDong
	# 				]
	default_urls = ["http://www.btapple.com"]
	default_user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	
	# Initialize
	vx = VxExtractor(default_user_agent)
	
	# 
	for url in default_urls:
		vx.init(url)
		vx.parseInfo('movie')
		#vx.parseInfo('ticket')
		#vx.saveDoc()