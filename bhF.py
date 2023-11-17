import smbus
import time
import jsonFuncs

bus = smbus.SMBus(1)

def convertToNumber(data):
	result=(data[1] - (256 * data[0])) / 1.2
	return result

def readLight(addr=0x23)
	data = bus.read_i2c_block_data(addr,0x10)
	jsonFuncs.storeData("lightLevels.JSON", {"time": time.time(), "lightLevel":convertToNumber(data)})
	return convertToNumber(data)
