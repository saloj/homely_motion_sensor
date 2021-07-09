import pycom
import time
from machine import Pin
from machine import Timer

pycom.heartbeat(False)

# config
motionDetected = 1
noMotionDetected = 0
hold_time_sec = 0.2
pir = Pin('P23', mode = Pin.IN)
green = 0x00FF00  # green
red = 0xFF0000  # red
chrono = Timer.Chrono() # measure the amount of time that has passed

def alert():
    print(chrono.read(), "Motion Detected!")
    print(pir())
    pycom.rgbled(red)
    time.sleep(5) # sleep for 5 seconds after detection
    pycom.rgbled(green)

# start detection
chrono.start()
pycom.rgbled(green)
print("Starting Detection...")

while True:
    if pir() == motionDetected:
        alert()
    else:
        pass

    time.sleep(hold_time_sec)
