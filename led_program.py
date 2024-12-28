#WAP to turn on LED when switch is pressed
#turn off led when switch is released

from machine import Pin
#import time

led=Pin(2,Pin.OUT)   #define pin for led

sw=Pin(0,Pin.IN)     #define pin for switch (pushbutton)


while(1):                     #loop
    if (sw.value()==0):       #if switch is pressed: value=0
        led.on()              #turn on led
    else:                     #if (sw.value()==1):----#if switch is released: value=1
        led.off()             #turn off led
