import dht
import machine
import time

#define the DHT11 sensor pin
#dht_pin=14         #replace with the GPIO pin to which your DHT1

#create a DTH object
dht11 = dht.DHT11(machine.Pin(14))        #or also write 'dht.DHT11(machine.Pin(dht_pin))' #DHT11 is the class

while True:
        dht11.measure()    #trigger a measurement
        
        #read temperature and humidity
        temp = dht11.temperature()
        humid = dht11.humidity()
        
        #print(Statements)
        print('Temperature = ',temp,'C')
        print('Humidity = ', humid)
        
        time.sleep(2) #wait before nect measurement