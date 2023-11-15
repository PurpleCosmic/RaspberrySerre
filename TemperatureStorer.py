import json
import time

current_weather = {
	"time":time.time(),
	"humidity":54,
	"temperature":1
}

with open("weather_data.json", "w") as file:
	json.dump(current_weather, file)
