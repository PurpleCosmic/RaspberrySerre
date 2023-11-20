import json
from os import path

def insertData(file, data):
	with open(file, "w") as writeFile:
		json.dump(data,  writeFile)

def createFile(filename):
	insertData(filename, [])

def readFile(file):
	if path.isfile(file) is False:
		createFile(file)

	data = []
	with open(file,"r") as readFile:
		data = json.load(readFile)
	return data

def storeData(file, data):
	d = readFile(file)
	d.append(data)

	insertData(file, d)
