try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

from time import sleep

print('setting everything up!')

# BCM -> broadcom pinout
# Board -> raspberry pi board piout

GPIO.setmode(GPIO.BOARD)


# Channel setup pin 37 -> GPIO26!
channel = 37 
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Polling loop
while True:
    if GPIO.input(channel):
        print('Input was HIGH')
    else:
        print('Input was LOW')
    sleep(1)
