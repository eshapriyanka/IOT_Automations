#libraries
import machine
import time

#pin: 15
ldr=machine.Pin(15,machine.Pin.IN)

#logic
while(True):              #0.1, 0+4j, '0', '0.0' ---> True values
    if(ldr.value()==0):   #{}, None, False, 0, 0.0, (), [], "" ---> False values
        print("There is a light, it's morning!!")
    else:
        print("It's dark! It's night")
    time.sleep(2)