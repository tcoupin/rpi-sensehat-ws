from sense_hat import SenseHat
import math
import time
import datetime

sense = SenseHat()
sense.clear()

sense.low_light = False
red = [255, 0, 0]
magenta = [255, 0, 100]
green = [0, 255, 0]
O = [0, 0, 0]

def resetPixel():
	return [
			O, O, O, O, O, O, O, O,
			O, O, O, O, O, O, O, O,
			O, O, O, O, O, O, O, O,
			O, O, O, O, O, O, O, O,
			O, O, O, O, O, O, O, O,
			O, O, O, O, O, O, O, O,
			O, O, O, O, O, O, O, O,
			O, O, O, O, O, O, O, O
			]


def aiguille(size, color,base, value):
	value-=base/4
	for i in range(size+1):
		x = min(int(round(3.5+i*math.cos(2*value*math.pi/base))),7)
		y = min(int(round(3.5+i*math.sin(2*value*math.pi/base))),7)
		pixels[x+8*y] = color

while True:
	pixels = resetPixel()
	now = datetime.datetime.now()
	aiguille(2,red,12,now.hour%12)
	aiguille(3,magenta,60,now.minute)
	aiguille(4,green,60,now.second)
	sense.set_pixels(pixels)
	#time.sleep(0.9)

#for i in range(60):
#	pixels=resetPixel()
#	aiguille(4,red,60,i)
#	time.sleep(0.01)