import RPi.GPIO as GPIO
import time
 

# config
SENSOR_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

# function to execute when movement is detected
def callback(channel):
    print('Cat movement detected!')

# start event/motion detection
try:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=callback)
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    print "Quit testing ..."

# cleanup GPIO stuff
GPIO.cleanup()
