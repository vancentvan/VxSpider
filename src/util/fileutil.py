import os, lxml

from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve

# Create directory for target path
def createDir(path):
	if not os.path.exists(path):
		file = os.mkdir(path)

# Delete files under target directory
def emptyDir(dir):
	for file in os.listdir(dir):
		del_file = os.path.join(dir, file)
		if os.path.isfile(del_file):
			os.remove(del_file)

# Save file from URL
def saveFile(path, url):
	createDir( "../" + path)
	# Store image URL
	image = []
	# Read all contents in a doc
	doc = urlopen(url).read()
	soup = BeautifulSoup(doc, "lxml")
	# Save target files, http://img.ivsky.com/img/tupian/li/201709/24/yueqiu-002.jpg
	for link in soup.find_all('img'):		
		imgUrl = link.get('src')
		image.append(imgUrl)
	
	for item in image:
		name = item.split('/')[-1]
		urlretrieve(item, "../" + path + '/' + name)