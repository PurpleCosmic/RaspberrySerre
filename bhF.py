#import smbus
import time
import jsonFuncs

import random
print("This is the testing version of bhF, values will be randomly generated")

#bus = smbus.SMBus(1)

def convertToNumber(data):
	result=(data[1] - (256 * data[0])) / 1.2
	return result

def readLight(addr=0x23)
	data = random.random()*200
	jsonFuncs.storeData("lightLevelsT.JSON", {"time": time.time(), "lightLevel":convertToNumber(data)})
	return convertToNumber(data)
