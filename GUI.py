##------------------
#Imports
from tkinter import *
import dhtF
import time
import datetime
import threading

##------------
#Constants (Deze mogen veranderd worden)
UPDATE_COOLDOWN = 10.0

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
	font = ("Helvetica",18),
)
tempValLabel.pack(fill=X, expand = 1, side = LEFT)

humidityValLabel = Label(frame,
	text = "Humidity:\n",
	font = ("Helvetica", 18)
)
humidityValLabel.pack(fill=X, expand=1, side = RIGHT)

dateLabel = Label(frame,
	text = "",
	font = ("Helvetica",24),
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
	timeText = str(currentTime.hour) + ":" + str(currentTime.minute)
	if currentTime.minute < 10:
		timeText = timeText[:len(timeText)-1] + "0" + timeText[1:]
	dateLabel.config(text=dateText+"\n"+timeText)

def dhtLoopFunc():
	time.sleep(3) #Give DHT time to start up
	while True: #Idem timeLoop
		try:
			updateDHTLabels()
			time.sleep(UPDATE_COOLDOWN)
		except:
			print("Failed To Update!\nRetrying")

def timeLoopFunc():
	while True: # I still need to find a way to kill this thread cuz it's not working
		updateTimeLabels()
		time.sleep(60)

dhtRunning = True
dhtThread = threading.Thread(target=dhtLoopFunc)
dhtThread.start()

dateRunning = True
timeThread = threading.Thread(target=timeLoopFunc)
timeThread.start()

def exitFunction():
	tk.destroy()

##-------
#Buttons

updateButton = Button(frame, text = "Update", command = updateDHTLabels)
updateButton.pack(side=BOTTOM)

exitButton = Button(frame, text = "Exit", command=exitFunction)
exitButton.pack(side=BOTTOM, before=updateButton)

tk.mainloop()
