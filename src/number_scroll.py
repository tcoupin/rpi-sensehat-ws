from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

x = '0'
R = '1'
matrix=[
	[
		x, R, x, x,
		R, x, R, x,
		R, x, R, x,
		R, x, R, x,
		x, R, x, x
	],
	[
		x, R, x, x,
		R, R, x, x,
		x, R, x, x,
		x, R, x, x,
		R, R, R, x
	],
	[
		R, R, R, x,
		x, x, R, x,
		x, R, x, x,
		R, x, x, x,
		R, R, R, x
	],
	[
		R, R, R, x,
		x, x, R, x,
		x, R, R, x,
		x, x, R, x,
		R, R, R, x
	],
	[
		x, R, x, x,
		R, x, x, x,
		R, x, x, x,
		R, R, R, x,
		x, R, x, x
	],
	[
		R, R, R, x,
		R, x, x, x,
		R, R, x, x,
		x, x, R, x,
		R, R, R, x
	],
	[
		x, R, x, x,
		R, x, x, x,
		R, R, x, x,
		R, x, R, x,
		x, R, x, x
	],
	[
		R, R, R, x,
		x, x, R, x,
		x, R, x, x,
		x, R, x, x,
		x, R, x, x
	],
	[
		x, R, x, x,
		R, x, R, x,
		x, R, x, x,
		R, x, R, x,
		x, R, x, x
	],
	[
		x, R, x, x,
		R, x, R, x,
		x, R, R, x,
		x, x, R, x,
		R, R, x, x
	],
	[
		x, x,
		x, x,
		x, x,
		x, x,
		R, x
	]
]


def show_number(number,text_colour=[255,255,255],back_colour=[0,0,0],scroll_speed=0.1, pixels=False):
	lignes = [[], [], [], [], []]

	# Prepend 8 back_colour c
	for i in range(8):
		for ligne in range(5):
			lignes[ligne]+=back_colour
	for i in number:
		if i=='.':
			i=10
		else:
			i=int(i)

		for ligne in range(5):
			lignes[ligne]+=matrix[i][(ligne*(len(matrix[i])/5)):((ligne+1)*(len(matrix[i])/5))]

		
		
#	for i in range(8):
#		for ligne in range(5):
#			lignes[ligne]+=back_colour
			
	for i in range(len(lignes[0])):
		for ligne in range(5):
			lignes[ligne][i]=text_colour if lignes[ligne][i]=='1' else back_colour;

	mpixels = [
		back_colour, back_colour, back_colour, back_colour, back_colour, back_colour, back_colour, back_colour,
		back_colour, back_colour, back_colour, back_colour, back_colour, back_colour, back_colour, back_colour,
		back_colour, back_colour, back_colour, back_colour, back_colour, back_colour, back_colour, back_colour,
		back_colour, back_colour, back_colour, back_colour, back_colour, back_colour, back_colour, back_colour,
		back_colour, back_colour, back_colour, back_colour, back_colour, back_colour, back_colour, back_colour,
		back_colour, back_colour, back_colour, back_colour, back_colour, back_colour, back_colour, back_colour,
		back_colour, back_colour, back_colour, back_colour, back_colour, back_colour, back_colour, back_colour,
		back_colour, back_colour, back_colour, back_colour, back_colour, back_colour, back_colour, back_colour
	]
	if pixels != False:
		mpixels[0:(len(pixels))]=pixels[:]



	for step in range (0,len(lignes[0])-8):
		for ligne in range(5):
			mpixels[3*8+(ligne*8):3*8+(ligne+1)*8]=lignes[ligne][step:step+8]
		sense.set_pixels(mpixels)
		time.sleep(scroll_speed)
	time.sleep(1)
	for step in range (len(lignes[0])-9,15,-1):
		for ligne in range(5):
			mpixels[3*8+(ligne*8):3*8+(ligne+1)*8]=lignes[ligne][step:step+8]
		sense.set_pixels(mpixels)
		time.sleep(scroll_speed)
