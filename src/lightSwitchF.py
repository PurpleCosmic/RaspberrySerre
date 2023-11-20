lightStatus = False

def getLightStatus():
	return lightStatus

def formatLightStatus():
	if lightStatus:
		return "On"
	else:
		return "Off"

def toggleLight():
	global lightStatus
	lightStatus = not lightStatus
	# Insert light toggle here
