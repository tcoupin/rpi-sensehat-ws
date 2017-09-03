from number_scroll import *
from sense_hat import SenseHat

sense = SenseHat()

RED=[200,0,0]
BLU=[0,0,200]
GRE=[0,200,0]

BRE=[0,50,50]
BBL=[50,50,0]
BGR=[50,0,50]

BLA=[0,0,0]

TEMP= [
	BRE, RED, RED, RED, BRE, BRE, BRE, BRE, 
	BRE, BRE, RED, BRE, BRE, RED, BRE, BRE, 
	BRE, BRE, RED, BRE, BRE, RED, BRE, BRE 
]
HUMI= [
	BBL, BLU, BBL, BLU, BBL, BBL, BBL, BBL, 
	BBL, BLU, BLU, BLU, BBL, BLU, BBL, BBL, 
	BBL, BLU, BBL, BLU, BBL, BLU, BBL, BBL 
]
PRES= [
	BGR, GRE, GRE, BGR, BGR, BGR, BGR, BGR, 
	BGR, GRE, GRE, BGR, GRE, BGR, BGR, BGR, 
	BGR, GRE, BGR, BGR, GRE, BGR, BGR, BGR 
]



temp = sense.get_temperature()
print('Temp: %s' % temp)
show_number(str(round(temp,1)), text_colour=RED, back_colour=BRE, pixels=TEMP)

humi = sense.get_humidity()
print('Humi: %s' % humi)
show_number(str(round(humi,1)), text_colour=BLU, back_colour=BBL, pixels=HUMI)


pres = sense.get_pressure()
print('Pres: %s' % pres)
show_number(str(round(pres,1)), text_colour=GRE, back_colour=BGR, pixels=PRES)

sense.clear()