##------------------
#Imports
from tkinter import *
import dhtF
import bhF
import time
import datetime
import threading
import lightSwitchF
import graphData

##------------
#Constants (Deze mogen veranderd worden)
UPDATE_COOLDOWN = 5.0

#Script Variables

##-------------
#Tk setup

tk = Tk()
tk.attributes('-fullscreen', True)
tk.title('Dashboard Serre')

##-------------
#Labels

frame = Frame(tk, borderwidth=2)
frame.pack(fill=BOTH, expand=1)

tempValLabel = Label(frame,
	text = "Temperature:\n",
	font = ("Helvetica",24),
)
tempValLabel.pack(fill=X, expand = 1, side = LEFT)

humidityValLabel = Label(frame,
	text = "Humidity:\n",
	font = ("Helvetica", 24)
)
humidityValLabel.pack(fill=X, expand=1, side = RIGHT)

dateLabel = Label(frame,
	text = "",
	font = ("Helvetica",32),
	bd = 1,
)
dateLabel.pack(side=TOP, pady = 20)

##-----------
#Functions

def updateDHTLabels():
	print("Updating DHT values")
	data = dhtF.readData()
	tempValLabel.config(text = "Temperature:\n"+dhtF.formatTemperature(data["temperature"]))
	humidityValLabel.config(text = "Humidity:\n"+dhtF.formatHumidity(data["humidity"]))

def updateTimeLabels():
	print("Updating Time labels")
	currentTime = datetime.datetime.now()
	dateText = str(currentTime.day) + " " + str(currentTime.strftime("%b")) + " " + str(currentTime.year)
	timeText = "{:02d}:{:02d}".format(currentTime.hour, currentTime.minute)
	dateLabel.config(text=dateText+"\n"+timeText)

def sensorLoopFunc():
	time.sleep(3) #Give DHT time to start up
	global running
	while running:
		try:
			updateDHTLabels()
			light = bhF.readLight()
			time.sleep(UPDATE_COOLDOWN)
		except:
			print("Failed To Update!\nRetrying")
	return

def timeLoopFunc():
	global running
	firstRead = True
	while running:
		updateTimeLabels()
		if firstRead:
			while not(time.time()%60 == 0):
				time.sleep(1)
		else:
			time.sleep(60)
	return

def toggleLight():
	lightSwitchF.toggleLight()
	lightButton.config(text = "Light:\n"+lightSwitchF.formatLightStatus())

running = True
dhtThread = threading.Thread(target=sensorLoopFunc)
dhtThread.start()

running = True
timeThread = threading.Thread(target=timeLoopFunc)
timeThread.start()

def exitFunction():
	global running
	running = False
	tk.destroy()

##-------
#Buttons

plotHumidButton = Button(frame, text = "Show Graph:\nHumidity", font=("Helevetica", 24), command = graphData.plotHumidity)
plotHumidButton.pack(side=RIGHT)

plotTempButton = Button(frame, text = "Show Graph:\nTemperature", font=("Helevetica", 24), command = graphData.plotTemperature)
plotTempButton.pack(side=LEFT)

plotLightButton = Button(frame, text = "Show Graph:\nLight Level", font=("Helevetica", 32), command = graphData.plotLight)
plotLightButton.pack(side=TOP)

lightButton = Button(frame, text = "Light:\n"+lightSwitchF.formatLightStatus(), font=("Helevetica", 32), command = toggleLight)
lightButton.place(anchor = CENTER, relx = .5, rely = .5)

updateButton = Button(frame, text = "Update", font=("Helvetica", 32), command = updateDHTLabels)
exitButton = Button(frame, text = "Exit", font=("Helvetica", 32), command=exitFunction)

exitButton.pack(side = BOTTOM)
updateButton.pack(side = BOTTOM)

tk.mainloop()
