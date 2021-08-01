# boot.py -- run on boot-up
from network import WLAN
import machine
import keys
wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
for net in nets:
    if net.ssid == keys.wifi_ssid: # if a WiFi network matching the ssid specified in keys.py is found
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, keys.wifi_password), timeout=5000) # attemps to authorize against the network using the password in keys.py
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break