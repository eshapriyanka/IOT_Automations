#WAP to calculate and display the distance of the object

import machine as m
import time as t

tri_pin=5
echo_pin=18

trigger=m. Pin(tri_pin, m.Pin.OUT)  #output pin
echo= m.Pin(echo_pin, m.Pin.IN)     #input pin

while True:
    #trigger pin high for us  and then low
    trigger.value(1)
    t.sleep_us(10)
    trigger.value(0)
    
    #record the initial time when echo is 1
    while echo.value()==0:
        pass
    initial_time = t.ticks_us()
    
    #record final time when echo is 0: sound waves hit receiver
    while echo.value() ==1:
        pass
    final_time = t.ticks_us()
    
    #actual time: from sound burst to hit back the receiver
    actual_time= t.ticks_diff(final_time, initial_time)
    
    #time at which sound waves hit the object
    tt= (actual_time/2)
    
    '''calculate distance with speed equation
    speed = distance/time
    speed of sound = 343m/s
    time=tt
    distance=343m/s*tt
    *As HC-SR04, range is 2cm-400cm, convert 343m/s  to cm/us
    343m/s=34300/1000000 cm/us'''
    
    distance_object= (34300*tt/1000000)
    
    print("Object is at a distance of", distance_object, "cm")
    
    #delay between two readings
    t.sleep(3)
    
    
'''def measure_distance():
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)
    
    #wait for the echo pin to go high
    while echo.value()==0:
        pass
    pulse_start = time.ticks_us() #time.time()--epoch time
    
    #wait for the echo pin to go low
    while echo.value() ==1:
        pass
    pulse_end = time.ticks_us()
    
    #calculate the duration of the pulse
    pulse_duration = time.ticks_diff(pulse_end,pulse_start)
    
    distance_cm=(pulse_duration*34300)/(2*1000000) #convert m to cm and s to us
    
    return distance_cm'''
        
    
    