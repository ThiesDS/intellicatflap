import RPi.GPIO as GPIO
import time
 

# config
SENSOR_PIN = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

# function to execute when movement is detected
def callback(channel):
    print('Cat movement detected!')

# start event/motion detection
try:
    while True:
        GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=callback)
        time.sleep(5)
except KeyboardInterrupt:
    print("Quit testing ...")

# cleanup GPIO stuff
GPIO.cleanup()
