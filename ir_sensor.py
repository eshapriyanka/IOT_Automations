from machine import Pin
from time import sleep

IR_PIN=15

ir_sense = Pin(IR_PIN, Pin.IN, Pin.PULL_UP)

while True:
    if ir_sense.value()==0:
        print("Object detected!")
    else:
        print("Object not detected")
    sleep(1)