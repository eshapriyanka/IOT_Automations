import network
import time

#Replace with your Wifi credentials
WIFI_SSID= "Galaxy priyanka"    #wifi name: SSID: Service Set Identifier
WIFI_PASSWORD= "9012345678"

wifi= network.WLAN(network.STA_IF)
#AP_IF: Accesspoint mode: creates own WLAN

if not wifi.isconnected():
    print("Connecting to WiFi...")
    wifi.active(True)              #activate interface, if False it's disconnectied
    wifi.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wifi.isconnected():
        pass
if wifi.isconnected():
    print("Connected to Wifi:", wifi.ifconfig())
else:
    print("Failed to connect to Wi-Fi!!!")
    wifi.active(False) #deactive the interface
    