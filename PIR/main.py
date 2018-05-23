try:
    import RPi.GPIO as GPIO
    from picamera import PiCamera
    import pygame
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

from time import sleep, time
import datetime
import firebase

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


def snapshot():
    #Taking a picture with the piCamera
    print('Get ready!')
    camera.start_preview()
    sleep(2)
    camera.capture('./image_%s.jpg' % getTime())
    camera.stop_preview()
    print('Snapped!')

def playFile():
    # Initializing sounds
    # White noise is heard if the mixer is kept initialized
    print('Quack!!!')
    pygame.mixer.init(48000, -16, 1, 1024)
    pygame.mixer.music.load("1.mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        pass
    pygame.mixer.quit()
    print('Bye Quack!!!')

def getTime():
    # Returns a timestamp
    ts = time();
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S')
    return st


def actions(ok):
    # Lets do more than one thing at the time
    #snapshot()
    playFile()

GPIO.add_event_detect(channel, GPIO.RISING, callback=actions)

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
