#LED Pragramming
#--------------------

#GPIO2
#WAP to blink: connected to pin2
from machine import Pin
import time

#machine: Pin: Pin(number, OUT/IN)
#select the GPIO pin: 2 as OUTPUT
led=machine.Pin(2, Pin.OUT)
#i=1
#while(i<=5):                        #looping for 5 times
for i in range(10):
    print("Led blink', i, 'time")
    led.on()                 #set pin to "on" (high) level
    time.sleep(2)            #delay
    led.off()                 #set pin to "off" (low) level
    time.sleep(2)            #delay
    #i=i+1
