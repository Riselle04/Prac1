#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <Riselle Rawthee>
Student Number: <RWTRIS001>
Prac: <1>
Date: <22/07/2019>
"""

# import Relevant Librares
try:
   import RPi.GPIO as GPIO
   print("importing GPIO complete")
   from time import sleep
   print("importing sleep complete")
   from itertools import product
except RuntimeError:
   print("error with GPIO and sleep import")
global counter
counter=0

def callback_increment(channel):
  global counter
  counter+=1
  if counter==8:
      counter=0
  GPIO.output(33,binArr[counter][0])
  GPIO.output(36, binArr[counter][1])
  GPIO.output(37, binArr[counter][2])
  print counter
  

def callback_decrement(channel):
 global counter
 counter-=1
 if counter==-1:
    counter=7
 GPIO.output(33,binArr[counter][0])
 GPIO.output(36, binArr[counter][1])
 GPIO.output(37, binArr[counter][2])
 print counter


 
def main():
 GPIO.setwarnings(False)
 global counter


GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.output(33,0)
GPIO.output(36,0)
GPIO.output(37,0)


binArr= list(product([0,1], repeat=3))

GPIO.add_event_detect(7, GPIO.FALLING, callback= callback_increment, bouncetime=100) 
GPIO.add_event_detect(13, GPIO.FALLING, callback= callback_decrement, bouncetime=100)

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
           main()
        GPIO.output(33,0)
        GPIO.output(36,0)
        GPIO.output(37,0)
        GPIO.cleanup()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except:
        print("Some other error occurred")
