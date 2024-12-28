#libraries
import machine as m
import time as t

#pin
buzz=m.Pin(16, m.Pin.OUT)

#loop
for i in range(5):         #infinite loop
    buzz.on()       #turn on buzzer: value=1
    t.sleep(0.2)
    print("Buzzer beeping!!!")
    
    buzz.off()
    t.sleep(1)      #turn off buzzer: value=0