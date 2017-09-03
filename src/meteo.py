from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()
print('Temp: %s' % temp)
sense.show_message('T: '+str(round(temp,1))+'C', text_colour=[255,0,0])

humi = sense.get_humidity()
print('Humi: %s' % humi)
sense.show_message('H:'+str(round(humi,1))+'%', text_colour=[0,0,255])

pres = sense.get_pressure()
print('Pres: %s' % pres)

sense.show_message('P:'+str(round(pres,0))+'hPa', text_colour=[0,255,0])