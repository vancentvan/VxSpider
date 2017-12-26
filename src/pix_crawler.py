import os

from util.fileutil import saveFile


def anaylizeUrl(path, url):
	saveFile(path, url)


if __name__ == '__main__':

	save_path = 'data/image'
	default_url = "http://www.ivsky.com/tupian/ziranfengguang/"
	
	anaylizeUrl( save_path, default_url )