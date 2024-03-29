import matplotlib.pyplot as plt
import jsonFuncs
import datetime

plt.grid(True)

X_COUNT = 12

def interpolateTimeValues(arr):
	minVal = min(arr)
	maxVal = max(arr)
	valArr = []
	diff = (maxVal-minVal)/(X_COUNT)

	for i in range(X_COUNT+1):
		valArr.append(minVal + i*diff)

	return valArr

def plotTimedData(file, dataKey, dataLabel, color):
	data = jsonFuncs.readFile(file)

	xAxis = [key["time"] for key in data]
	yAxis = [key[dataKey] for key in data]

	valArray = interpolateTimeValues(xAxis)

	timeValues = ["{:02d}:{:02d}".format(datetime.datetime.fromtimestamp(key).hour, datetime.datetime.fromtimestamp(key).minute) for key in valArray]
	plt.xticks(valArray, timeValues)

	plt.plot(xAxis, yAxis, color = color, marker = 'o')
	plt.xlabel('time')
	plt.ylabel(dataLabel)

	plt.show()

def plotLight():
	plotTimedData("lightLevels.JSON", "lightLevel", "Light Level", 'y')

def plotHumidity():
	plotTimedData("dht_data.JSON", "humidity", "Humidity", 'b')

def plotTemperature():
	plotTimedData("dht_data.JSON", "temperature", "Temperature", 'r')
