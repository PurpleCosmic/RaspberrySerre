##------------------
#Imports
from tkinter import *
import dhtF
import time
import datetime
import threading

tk = Tk()

##------------
#Constants (Deze mogen veranderd worden)
UPDATE_COOLDOWN = 10.0

#Script Variables
Active = True

##-------------
#Labels

frame = Frame(tk, borderwidth=2)
frame.pack(fill=BOTH, expand=1)

tempLabel = Label(frame, text="")
tempLabel.pack(fill=X, expand = 1, side = LEFT)

humidityLabel = Label(frame, text = "")
humidityLabel.pack(fill=X, expand=1, side = RIGHT)

dateLabel = Label(frame, text = "")
timeLabel = Label(frame, text = "")
dateLabel.pack(side=TOP)
timeLabel.pack(side=TOP)

##-----------
#Functions

def updateDHTLabels():
	print("Updating DHT values")
	data = dhtF.readData()
	tempLabel.config(text = dhtF.formatTemperature(data["temperature"]))
	humidityLabel.config(text = dhtF.formatHumidity(data["humidity"]))

def updateTimeLabels():
	print("Updating Time labels")
	currentTime = datetime.datetime.now()
	dateLabel.config(text=str(currentTime.day) + " " + str(currentTime.strftime("%b")) + " " + str(currentTime.year))
	timeLabel.config(text=str(currentTime.hour) + ":" + str(currentTime.minute))

def dhtLoopFunc():
	time.sleep(3)
	while Active:
		print(Active)
		try:
			updateDHTLabels()
			time.sleep(UPDATE_COOLDOWN)
		except:
			print("Failed To Update!\nRetrying")

def timeLoopFunc():
	while Active:
		updateTimeLabels()
		time.sleep(60)

dhtThread = threading.Thread(target=dhtLoopFunc)
dhtThread.start()

timeThread = threading.Thread(target=timeLoopFunc)
timeThread.start()

def exitFunction():
	Active = False
	tk.destroy()

##-------
#Buttons

updateButton = Button(frame, text = "Update", command = updateDHTLabels)
updateButton.pack(side=BOTTOM)

exitButton = Button(frame, text = "Exit", command=exitFunction)
exitButton.pack(side=BOTTOM, before=updateButton)

tk.mainloop()
