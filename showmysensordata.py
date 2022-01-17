from sense_hat import SenseHat
sense= SenseHat()

while True:
    #Take readings from all three sensors
    t=sense.get_temperature()
    p=sense.get_pressure()
    h=sense.get_humidity()

#Display text message
    message = "Temperature: "+t+"Pressure: "+p+"Humidity: "+h
    
    sense.show_message(message,speed_scroll=0.05)