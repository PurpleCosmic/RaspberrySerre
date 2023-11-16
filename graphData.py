import matplotlib.pyplot as plt
import jsonFuncs

plt.grid(True)

def plotTimedData(file, dataKey, dataLabel, color):
	data = jsonFuncs.readFile(file)

	xAxis = [key["time"] for key in data]
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
