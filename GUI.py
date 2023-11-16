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

tempValLabel = Label(frame, text="")
tempValLabel.pack(fill=X, expand = 1, side = LEFT)

humidityValLabel = Label(frame, text = "")
humidityValLabel.pack(fill=X, expand=1, side = RIGHT)

dateLabel = Label(frame, text = "")
timeLabel = Label(frame, text = "")
dateLabel.pack(side=TOP)
timeLabel.pack(side=TOP)

##-----------
#Functions

def updateDHTLabels():
	print("Updating DHT values")
	data = dhtF.readData()
	tempValLabel.config(text = dhtF.formatTemperature(data["temperature"]))
	humidityValLabel.config(text = dhtF.formatHumidity(data["humidity"]))

def updateTimeLabels():
	print("Updating Time labels")
	currentTime = datetime.datetime.now()
	dateLabel.config(text=str(currentTime.day) + " " + str(currentTime.strftime("%b")) + " " + str(currentTime.year))
	timeText = str(currentTime.hour) + ":" + str(currentTime.minute)
	if currentTime.minute < 10:
		timeText = timeText[:len(timeText)-1] + "0" + timeText[1:]
	timeLabel.config(text=str(currentTime.hour) + ":" + str(currentTime.minute))

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
