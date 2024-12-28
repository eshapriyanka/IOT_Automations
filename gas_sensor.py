'''to calculate required Voltage change for one
level change in output
5/4095=0.0012v=1.2mV
0V --> 0
1.2mV --> 1
2.4mV --> 2
3.6mV --> 3
..
..
5V --> 4095
'''

from machine import Pin, ADC
import time

#define the pin to which the analog output of the
mq2_analog_pin=34 #change this pin number as

#define the threshold voltage (you might need to 
threshold_voltage = 1.5 #adjust this value accordingly

#create an ADC object
adc = ADC(Pin(mq2_analog_pin))

while True:
    #read the raw ADC value from the MQ-3 sensor
    raw_value = adc.read()
    
    #Calculate the voltage based on the raw ADC voltage
    voltage = (raw_value/4095) * 3.3 #ESP32 ADC
    
    #check if the voltage crosses the threshold
    if voltage > threshold_voltage:
        print("Gas leak detected!")
    else:
        print("No gas leak detected.")
        
    #wait for some time before taking 
    
    