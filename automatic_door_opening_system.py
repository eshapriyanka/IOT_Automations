#Automatic Door opening system

from machine import Pin, PWM
import time

# Servo Motor Setup
servo_pin = Pin(23, Pin.OUT)
pwm_pin = PWM(servo_pin)
pwm_pin.freq(50)  # 50Hz: 1/50 = 0.02s = 20ms

# Map range of input angles to range of output duty cycles
def map_range(x, inmin, inmax, outmin, outmax):
    return int((x - inmin) * (outmax - outmin) / (inmax - inmin) + outmin)

def set_servo_angle(pwm_pin, angle):
    pwm_pin.duty(map_range(angle, 0, 180, 20, 120))

# IR Sensor Setup
IR_PIN = 15
ir_sensor = Pin(IR_PIN, Pin.IN, Pin.PULL_UP)

# Initial Servo Position (Door Closed)
set_servo_angle(pwm_pin, 0)  # Door closed at 0 degrees
print("System initialized. Door is closed.")

while True:
    if ir_sensor.value() == 0:  # IR sensor detects someone
        print("Someone at the door")
        print("Opening the door...")
        set_servo_angle(pwm_pin, 90)  # Open the door to 90 degrees
        time.sleep(5)  # Keep the door open for 5 seconds
        print("Closing the door...")
        set_servo_angle(pwm_pin, 0)  # Close the door to 0 degrees
    else:
        print("No one at the door!")
    time.sleep(2)

'''import machine
import time

IR_PIN=15
data=machine.Pin(IR_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if data.value() ==0:
        print("Someone at the door")
        print("Opening the door")
    else:
        print("No one at the door")
    time.sleep(2)'''