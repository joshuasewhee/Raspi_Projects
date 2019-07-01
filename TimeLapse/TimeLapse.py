"""
Joshua Sew-Hee
6/30/19
Time Lapse
"""

# Include PiCamera, os and time library
from picamera import PiCamera
from time import sleep
from os import system
import os

# Create camera object
camera = PiCamera()

# Path to save image in
path = '/home/pi/Desktop/TimeLapses/'

# Make camera to be upright
camera.rotation = 180
camera.resolution = (1072,960)

for i in range(10):
    # Take picture and pad the number with zeros in the name, so that there are always 4 digits. 
    camera.capture(path + 'myTimeLapse{0:04d}.jpg'.format(i))
    sleep(2)
    print("Picture %d taken" %(1+i))
          
# Make a gif of the time lapse
os.chdir(path)
system('convert -delay 10 -loop 0 myTimeLapse*.jpg animation.gif')
print('Gif done')