#gas alarm
from machine import Pin,ADC
import time
#Define the pin to which the analog output of the !
mq2_analog_Pin = 34 #change this pin number as!
threshold_voltage=0.3
#create an ADC object
adc=ADC(Pin(mq2_analog_Pin))
buzz=Pin(16,Pin.OUT)
#while True:
for i in range(5):
    #Read the raw ADC value  from the MQ-3 sensor
    raw_value=adc.read()
    #calculate the voltage based on the raw ADC value
    voltage = raw_value / 4095 *3.3 #ESP32 ADC
    #check if the voltage crosses the threshold
    print(voltage)
    if voltage >threshold_voltage:
        print("Gas leak detected!")
        for i in range(1,6,1):
            buzz.on()
            time.sleep(0.2)
    #turn off buzzer:value=0
            buzz.off()
            time.sleep(0.1)
    else:
        print("No gas leak detected.")
        time.sleep(2)
        buzz.off()
        time.sleep(0.5)
        
#Connections!!
# sensors  ===  vcc-5v, gnd-gnd, DO-P15, AO- P34
# Buzzer === negative-gnd, postive-P16
#loop
#while(100):#finite times
    #100 is a true and also a string constiting of 0 is also a true value where as
    # zero, any empty data set ,false are flase values
    
    #turn on buzzer:value=1