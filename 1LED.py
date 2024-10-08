#Pin Connection

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
for i in range(5):
    GPIO.output(15,True)
    print("No")
    time.sleep(1)
print("Done")
GPIO.cleanup()
