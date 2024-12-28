import network
import time
import urequests

wifi_ssid= "Galaxy priyanka"
wifi_password= "9012345678"


def thing_read():
    #url='https://api.thingspeak.com/channels/2795276/feeds/last.json?api_key=AD1WM7VQCOKMA5SJ&results=2'
    url='https://api.thingspeak.com/channels/2795276/fields/4/last.json?api_key=AD1WM7VQCOKMA5SJ&results=2'
    
    
    print("Reading data from the cloud..")
    response=urequests.get(url)
    data=response.json()
    
    print('Data is:\n', data)
    
    f1=data.get('field1')
    f2=data.get('field2')
    f3=data.get('field3')
    f4=data.get('field4')
    
    print("Field1 ",f1)
    print("Field2 ",f2)
    print("Field3 ",f3)
    print("Field4 ",f4)
    
    response.close()
    
    
def wifi_setup():
    wifi=network.WLAN(network.STA_IF)

    if not wifi.isconnected():
        print("Connecting to WiFi!")
        wifi.active(True)
        wifi.connect(wifi_ssid,wifi_password)
        while not wifi.isconnected():
            pass
    if wifi.isconnected():
        print("Connected to wifi:",wifi.ifconfig())
        thing_read()
    else:
        print("Failed to connect to wifi")
        wifi.active(False)

wifi_setup()