from sense_hat import SenseHat
import math
import time
import datetime

sense = SenseHat()
sense.clear()
sense.set_rotation(270)

sense.low_light = True

red = [255, 0, 0]
magenta = [255, 0, 100]
green = [0, 255, 0]

O = [0, 0, 0]

def numbertoline(nb,bg,fg):
	binvalue=bin(int(nb))
	binvalue=binvalue[2:][::-1]+'00000000'
	binvalue=binvalue[0:8]
	line=[0,0,0,0,0,0,0,0]
	for i in range(8):
		if binvalue[i]=="1":
			line[i]=fg
		else:
			line[i]=bg
	return line

while True:
	now = datetime.datetime.now()
	matrix=[]
	matrix+=numbertoline(("%02d" % now.hour)[0:1],O,red)
	matrix+=numbertoline(("%02d" % now.hour)[1:2],O,red)
	matrix+=numbertoline(1,O,O)
	matrix+=numbertoline(("%02d" % now.minute)[0:1],O,red)
	matrix+=numbertoline(("%02d" % now.minute)[1:2],O,red)
	matrix+=numbertoline(1,O,O)
	matrix+=numbertoline(("%02d" % now.second)[0:1],O,red)
	matrix+=numbertoline(("%02d" % now.second)[1:2],O,red)
	sense.set_pixels(matrix)
	time.sleep(0.3)

#for i in range(60):
#	pixels=resetPixel()
#	aiguille(4,red,60,i)
#	time.sleep(0.01)