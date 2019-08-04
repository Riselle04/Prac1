#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <Riselle>
Student Number: <RWTRIS001>
Prac: <01>
Date: <26/07/19>
"""
# import Relevant Librares
import RPi.GPIO as GPIO
from time import sleep

def my_callback(channel):
  GPIO.output(11, GPIO.HIGH)
  sleep(1)
  GPIO.output(11, GPIO.LOW)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.OUT)    

# Logic that you write
def main():
 GPIO.setwarnings(False)
 
GPIO.add_event_detect(7, GPIO.FALLING, callback=my_callback, bouncetime=150)  



# Only run the functions if
if __name__ == "__main__":
 # Make sure the GPIO is stopped correctly
 try:
    while True:
      main()
    
 except KeyboardInterrupt:
    print("Exiting gracefully")
    # Turn off your GPIOs here
    GPIO.cleanup()
 except:
   print("Some other error occurred")
   GPIO.cleanup()

