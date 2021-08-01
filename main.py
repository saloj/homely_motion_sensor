# import the necessary libraries which contain functionality and functions
import pycom
import time
from machine import Pin
from machine import Timer

# turn off the blinking LED on the LoPy4
pycom.heartbeat(False)

# basic config setup to make the alert function cleaner and easier to read
motionDetected = 1
noMotionDetected = 0
hold_time_sec = 0.2
pir = Pin('P23', mode = Pin.IN) # if you connected the signal to any other pin, replace 'P23' with the one you're using
green = 0x00FF00  # green
red = 0xFF0000  # red
chrono = Timer.Chrono() # measure the amount of time that has passed since the program started to run

def alert():
    print(chrono.read(), "Motion Detected!") # prints time elapsed and a string to the console
    pybytes.send_signal(1, 1) # sends a signal to Pybytes. the first argument is the signal number specified on Pybytes, the second is just an integer representation of an event
    pycom.rgbled(red) # turns the LED red when detection has occurred
    time.sleep(5) # sleep for 5 seconds after detection
    pycom.rgbled(green) # turns the LED green

# start detection
chrono.start()
pycom.rgbled(green)
print("Starting Detection...")

# infinite loop, runs until terminated
while True:
    if pir() == motionDetected: # if the PIR sensor has been triggered, call the alert function
        alert()
    else:
        pass

    time.sleep(hold_time_sec) # wait for the specified amount of time to avoid cluttering and faulty readings
