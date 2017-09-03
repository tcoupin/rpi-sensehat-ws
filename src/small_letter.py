from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

sense.low_light = True
R = [255, 0, 0]
x = [0, 0, 0]

pixels = [
	x, R, x, x, R, R, R, x,
	R, R, x, x, x, x, R, x,
	x, R, x, x, x, R, x, x,
	x, R, x, x, R, x, x, x,
	R, R, R, x, R, R, R, x,
	x, x, x, x, x, x, x, x,
	x, x, x, x, x, x, x, x,
	x, x, x, x, x, x, x, x
]

sense.set_pixels(pixels)

time.sleep(1)

pixels = [
	R, R, R, x, x, R, x, x,
	x, x, R, x, R, x, x, x,
	x, R, R, x, R, x, x, x,
	x, x, R, x, R, R, R, x,
	R, R, R, x, x, R, x, x,
	x, x, x, x, x, x, x, x,
	x, x, x, x, x, x, x, x,
	x, x, x, x, x, x, x, x
]

sense.set_pixels(pixels)

time.sleep(1)

pixels = [
	R, R, R, x, x, R, x, x,
	R, x, x, x, R, x, x, x,
	R, R, x, x, R, R, x, x,
	x, x, R, x, R, x, R, x,
	R, R, R, x, x, R, x, x,
	x, x, x, x, x, x, x, x,
	x, x, x, x, x, x, x, x,
	x, x, x, x, x, x, x, x
]

sense.set_pixels(pixels)

time.sleep(1)

pixels = [
	R, R, R, x, x, R, x, x,
	x, x, R, x, R, x, R, x,
	x, R, x, x, x, R, x, x,
	x, R, x, x, R, x, R, x,
	x, R, x, x, x, R, x, x,
	x, x, x, x, x, x, x, x,
	x, x, x, x, x, x, x, x,
	x, x, x, x, x, x, x, x
]

sense.set_pixels(pixels)

time.sleep(1)

pixels = [
	x, R, x, x, x, R, x, x,
	R, x, R, x, R, x, R, x,
	x, R, R, x, R, x, R, x,
	x, x, R, x, R, x, R, x,
	R, R, x, x, x, R, x, x,
	x, x, x, x, x, x, x, x,
	x, x, x, x, x, x, x, x,
	x, x, x, x, x, x, x, x
]

sense.set_pixels(pixels)

time.sleep(1)

sense.show_message('1234567890')
sense.show_message('1234567890')
