from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

sense.low_light = True
x = [0, 0, 0]

def getPixels(R):
	return [
		x, R, R, x, x, R, R, x,
		R, x, x, R, R, x, x, R,
		R, x, x, R, R, x, x, R,
		R, x, x, x, x, x, x, R,
		R, x, x, x, x, x, x, R,
		x, R, x, x, x, x, R, x,
		x, x, R, x, x, R, x, x,
		x, x, x, R, R, x, x, x
	]

def tsv2rbv(t,s,v):
	ti = int(t/60)%6

	f=t/60-ti
	l=int(v*(1-s)*255)
	m=int(v*(1-f*s)*255)
	n=int(v*(1-(1-f)*s)*255)
	v=int(v*255)
	if ti ==0:
		return [v,n,l]
	elif ti==1:
		return [m,v,l]
	elif ti==2:
		return [l,v,n]
	elif ti==3:
		return [l,m,v]
	elif ti==4:
		return [n,l,v]
	elif ti==5:
		return [v,l,m]

for r in range(360):
	color=tsv2rbv(float(r),1.,0.5)
	sense.set_pixels(getPixels(color))
	time.sleep(0.01)

sense.clear()