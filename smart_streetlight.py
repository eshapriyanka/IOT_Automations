#smart street lighting System(Auto):
#LDR, LED, wifi, Thingspeak

import machine, time, network, urequests

def ldr_sensor():
    ldr_pin=machine.Pin(15,machine.Pin.IN)
    v=ldr_pin.value()
    return v

def street_light(f):
    f1=int(f)
    light_pin=machine.Pin(2,machine.Pin.OUT)
    if f1==0:
        print("It is Bright!!")
        print("Street Light is OFF")
        light_pin.off()
    else:
        print("It is Dark!!")
        print("Street Light is turning ON :-)")
        light_pin.on()


def Uploadind_data_to_Cloud(d):
    WRITE_API_KEY="FX084RYV08NUC320"
    api_url="http://api.thingspeak.com/update"
    data={
        "api_key":WRITE_API_KEY,
        "field1":d,
        }
    print("Uploading the data to the CLOUD..")
    response_cloud=urequests.post(api_url,json=data)
    print("ThingSpeak response:",response_cloud.text)
    
    response_cloud.close()
    print("Data is successfully uploaded")
    

def Retrieving_data_from_Cloud():
    #url='https://api.thingspeak.com/channels/2795878/feeds.json?api_key=DGUER7Z0K5VL30VA&results=2'
    url='https://api.thingspeak.com/channels/2795878/fields/1/last.json?api_key=DGUER7Z0K5VL30VA&results=2'
    print("Reading data from the cloud..")
    response=urequests.get(url)
    data=response.json()
    f1=data.get('field1')
    print("Retrieved data is = ",f1)
    street_light(f1)
    response.close()


def wifi_setup(data):
    wifi_ssid= "Galaxy priyanka"
    wifi_password= "9012345678"
    wifi=network.WLAN(network.STA_IF)
    if not wifi.isconnected():
        print("Connecting to WiFi!")
        wifi.active(True)
        wifi.connect(wifi_ssid,wifi_password)
        while not wifi.isconnected():
            pass
    if wifi.isconnected():
        print("Connected to wifi:",wifi.ifconfig())
        
        Uploadind_data_to_Cloud(data)
        time.sleep(3)
        Retrieving_data_from_Cloud()
        time.sleep(2)   
    else:
        print("Failed to connect to wifi")
        wifi.active(False)

print("Detecting if light or dark..")
sensed_value = ldr_sensor()
time.sleep(2)
print("Setting up the Wi-Fi....")
wifi_setup(sensed_value)
print("SMART STREET LIGHT is SUCCESSFULLY DESIGNED:)")
