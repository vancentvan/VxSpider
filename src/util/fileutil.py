import os

# Create directory for target path
def createDir(path):
	if not os.path.exists(path):
		os.mkdir(path)

# Delete files under target directory
def emptyDir(dir):
	for file in os.listdir(dir):
		del_file = os.path.join(dir, file)
		if os.path.isfile(del_file):
			os.remove(del_file)

# Save data(bytes) to file
def saveFile(path, data):
	with open(path, 'wb') as f:
		f.write(data)