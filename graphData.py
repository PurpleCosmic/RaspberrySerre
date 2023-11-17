import matplotlib.pyplot as plt
import jsonFuncs
import datetime

plt.grid(True)

def plotTimedData(file, dataKey, dataLabel, color):
	data = jsonFuncs.readFile(file)

	xAxis = ["{:02d}:{:02d}".format(datetime.datetime.fromtimestamp(key["time"]).hour, datetime.datetime.fromtimestamp(key["time"]).minute) for key in data]
	yAxis = [key[dataKey] for key in data]

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
