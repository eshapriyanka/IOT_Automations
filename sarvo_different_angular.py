from machine import Pin,PWM
import time

servo_pin=Pin(23,Pin.OUT)
pwm_pin=PWM(servo_pin)
pwm_pin.freq(50)   #50Hz: 1/50 = 0.02s = 20ms
pwm_pin.duty(0)

def map(x,inmin,inmax,outmin,outmax):
    return int((x-inmin)*(outmax-outmin)/(inmax-inmin)+outmin)

def servo(pwm_pin,angle):
    pwm_pin.duty(map(angle,0,180,20,120))

print("Rotating from 0 to 170")
for i in range(0,180,10):
    servo(pwm_pin,i)
    print("Angle : ",i)
    time.sleep(2)
    
print("Rotating from 170 to 0")
for i in range(170,0,-10):
    servo(pwm_pin,i)
    print("Angle : ",i)
    time.sleep(2)