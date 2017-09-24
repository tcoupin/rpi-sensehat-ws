from sense_hat import SenseHat
import sys,tty,termios

def readChar():
	fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

sense=SenseHat()
sig=True
print "Press @ to exit"
while sig:
	nb = readChar()
	if nb=='@':
		sig=False
	sense.show_letter(nb)
sense.clear()
