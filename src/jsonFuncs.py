import json
from os import path

def checkFileName(filename):
	if filename.find("data/") == -1:
		filename = "data/" + filename
	return filename

def insertData(filename, data):
	file = checkFileName(filename)
	with open(file, "w") as writeFile:
		json.dump(data,  writeFile)

def createFile(filename):
	file = checkFileName(filename)
	insertData(file, [])

def readFile(filename):
	file = checkFileName(filename)
	if path.isfile(file) is False:
		createFile(file)

	data = []
	with open(file,"r") as readFile:
		data = json.load(readFile)
	return data

def storeData(filename, data):
	file = checkFileName(filename)
	d = readFile(file)
	d.append(data)

	insertData(file, d)
