import network
import time
import urequests

wifi_ssid= "Galaxy priyanka"
wifi_password= "9012345678"

def thing_write():
    WRITE_API_KEY="CG04RB8U3RRYVCPL"
    api_url="http://api.thingspeak.com/update"
    data={
        "api_key":WRITE_API_KEY,
        "field1":12,
        "field2":28,
        "field3":25,
        "field4":20,
        }
    #upload the data using post function:
    print("Uploading the data to the CLOUD..")
    response_cloud=urequests.post(api_url,json=data)
    print("ThingSpeak response:",response_cloud.text)
    
    #close the connection
    response_cloud.close()
    print("Data is successfully uploaded")
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
        thing_write()
    else:
        print("Failed to connect to wifi")
        wifi.active(False)

wifi_setup()