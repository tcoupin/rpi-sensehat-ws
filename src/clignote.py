from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

for i in range(100):
	sense.show_letter("A", text_colour=[255,255,255])
	time.sleep(0.03)
	sense.show_letter("A", text_colour=[0,0,0], back_colour=[255,255,255])
	time.sleep(0.03)