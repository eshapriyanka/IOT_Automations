#pin: 14
import machine
import time

sm_pin=machine.Pin(14, machine.Pin.IN)

while(1):
    if(sm_pin.value()==0):
        print("Soil is wet")
    else:
        print("Soil is dry")
    time.sleep(2)