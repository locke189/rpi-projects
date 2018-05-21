try:
    import RPi.GPIO as GPIO
    from picamera import PiCamera
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

from time import sleep, time
import datetime

print('setting everything up!')

# BCM -> broadcom pinout
# Board -> raspberry pi board piout

GPIO.setmode(GPIO.BOARD)

# Camera on!
camera = PiCamera()

# Channel setup pin 37 -> GPIO26!
# Can also specify a lot of channels using a list
channel = 37
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def snapshot(channel):
    print('Get ready!')
    camera.start_preview()
    sleep(5)
    camera.capture('./image_%s.jpg' % getTime())
    camera.stop_preview()
    print('Snapped!')

def getTime():
    ts = time();
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S')
    print st

GPIO.add_event_detect(channel, GPIO.RISING, callback=snapshot)

try:
    while True:
        pass
except:
    # Closing up
    print('Cleaning up!')
    GPIO.cleanup(channel)


'''
# Polling loop
try:
    while True:
        if GPIO.input(channel):
            print('Input was HIGH')
        else:
            print('Input was LOW')
        sleep(1)
except:
    # Closing up
    GPIO.cleanup(channel)
'''
