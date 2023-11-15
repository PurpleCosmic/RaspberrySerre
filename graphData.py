import matplotlib.pyplot as plt
import jsonFuncs

plt.grid(True)

def plotLight():
	data = jsonFuncs.readFile("lightLevels.JSON")

	xAxis = [key["time"] for key in data]
	yAxis = [key["lightLevel"] for key in data]

	plt.plot(xAxis, yAxis, color = 'y', marker = 'o')
	plt.xlabel('time')
	plt.ylabel('Light Level')

	plt.show()

def plotHumidity():
	data = jsonFuncs.readFile("dht_data.JSON")

	xAxis = [key["time"] for key in data]
	yAxis = [key["humidity"] for key in data]

	plt.plot(xAxis, yAxis, color = 'b', marker = 'o')
	plt.xlabel('time')
	plt.ylabel('Humidity')

	plt.show()
	
def plotTemperature():
	data = jsonFuncs.readFile("dht_data.JSON")

	xAxis = [key["time"] for key in data]
	yAxis = [key["temperature"] for key in data]

	plt.plot(xAxis, yAxis, color = 'r', marker = 'o')
	plt.xlabel('time')
	plt.ylabel('Temperature')

	plt.show()	
