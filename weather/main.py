import eel
import pyowm

owm = pyowm.OWM('ba0b14b35c181a6b2c78c4b5bd860cc2')

@eel.expose
def get_weather(place):
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(place)
	w = observation.weather
	temperature = int(w.temperature('celsius')['temp'])

	return f"{temperature} degrees Celsius! "

eel.init('web')

eel.start('main.html', size=(700, 350))