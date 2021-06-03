import RPi.GPIO as GPIO
import time
import log


# Get logger
logger = log.get_logger(__name__, log_level='DEBUG', log_file_path='./', log_file_name='test_<YYYYmmdd>.logs')

# config
SENSOR_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

# initial setup
active = 0
movement = 0

# start event/motion detection
logger.info('Start test motion detection.')
try:
    while True:
        # read state
        movement = GPIO.input(SENSOR_PIN)
        logger.debug(f'Current sensor state: {movement}')

        # if movement detected, set active to 1
        if movement == 1 and active == 0:
            logger.info("Movement detected.")
            active = 1
 
        # if no movement detected anymore, set active to 0
        elif movement == 0 and active == 1:
            logger("No movement detected.")
            active = 0
        
        time.sleep(10)

except KeyboardInterrupt:
    logger.info("Quit testing on KeyboardInterrupt.")
    GPIO.cleanup()
