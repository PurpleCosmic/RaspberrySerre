import time
#import board
#import adafruit_dht
import jsonFuncs

import random
#dhtDevice = adafruit_dht.DHT22(board.D4)

def readData():
	success = False
	while not(success):
		try:
			data = {
				"time": time.time(),
				"temperature": random.random()*32+10, # dhtDevice.temperature,
				"humidity": random.random()*2 # dhtDevice.humidity
			}
			success = True
		except:
			print("Failed Fetching Data")
			time.sleep(1)
	jsonFuncs.storeData("dht_data.JSON", data)
	return data

def formatTemperature(t):
	return "{:.1f}C".format(
		t
	)

def formatHumidity(h):
	return "{:.2f}%".format(
		h
	)


