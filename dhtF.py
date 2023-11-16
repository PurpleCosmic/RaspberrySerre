import time
import jsonFuncs

import random

print("This is the testing version, values will be randomly generated")

def readData():
	success = False
	while not(success):
		try:
			data = {
				"time": time.time(),
				"temperature": random.random()*32 + 10,
				"humidity": random.random()*100
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


