# Joshua Sew-Hee
# 6/20/18
# This program shows the options available with the pi camera
# and allows the user to choose the effect wanted before
# taking the picture
# The image will be saved as the effect's name followed by
# the date and time when the picture was taken

# version 1: simple menu

# version 2:
# added a function for the camera menu
# change if statements in while loop to make it more efficient

# version 3:
# added text to image for brightness, constrast and max_res
# added delay to control time before taking picture in all modes

# version 4:
# made path easily editable
# fixed camera having effects overlaying on top of each other

# import necessay libraries
from picamera import PiCamera, Color
from time import sleep
from datetime import datetime

def cam_modes(modes):
    count = 0
    for mode in modes:
        if (count == 2):

            print("%15s" %mode)
            
            count = 0
        else:
            print("%15s" %mode, end=' ')
            count = count + 1
    

def camera_menu():
    print("brightness\tcontrast\tmax_res")

    effects = ['none', 'negative', 'solarize', 'sketch', 'denoise', 
    'emboss', 'oilpaint', 'hatch', 'gpen', 'pastel', 'watercolor', 'film', 
    'blur', 'saturation', 'colorswap', 'washedout', 'posterise', 'colorpoint', 
    'colorbalance', 'cartoon', 'deinterlace1', 'deinterlace2']

    print("\nEffect modes: ")
    #for effect in effects:
    #    print(effect, end = '\t')

    cam_modes(effects)

    awb_modes = ['off', 'auto', 'sunlight', 'cloudy',
    'shade', 'tungsten', 'fluorescent', 'incandescent',
    'flash', 'horizon']

    print("\n\nAutowhitebalance modes: ")
    #for awb_mode in awb_modes:
    #    print(awb_mode, end = '\t')
    cam_modes(awb_modes)    

    exposures = ['off', 'auto', 'night', 'nightpreview', 'backlight', 
    'spotlight', 'sports', 'snow', 'beach', 'verylong', 'fixedfps', 
    'antishake', 'fireworks']

    
    print("\n\nExposures modes: ")
    cam_modes(exposures)

    
print("Welcome to JSH Pi Camera.")
print("What would you like to do?")
print("Type one of the exact option names:")
camera_menu()

# gather current date and time add to picture name
current_date_time = datetime.now()
current_date_time = str(current_date_time)
element = current_date_time.split(' ')
date = element[0]
temp = element[1].split('.')
time = temp[0].replace(':','')   

# path to save image in
path = '/home/pi/Desktop/'    
# time before taking picture
delay = 2
# ask user for camera option
option = input("\nChoice? ")
# create an instance of the camera
camera = PiCamera()

while(option != "exit"):
    # close the camera to reset it
    camera.close()
    # re open the camera afresh
    camera = PiCamera()
    # for camera to be upright
    camera.rotation = 180
    # to alter the transparency of the camera preview by setting 
    # an alpha level, which can be chosen from 0 to 255
    camera.start_preview(alpha=75)
    # Valid sizes are 6 to 160.
    # The default is 32.
    camera.annotate_text_size = 50
    # backgroud of text box
    # camera.annotate_background = Color('blue')
    # color of text in text box
    # camera.annotate_foreground = Color('red')
    if(option == 'brightness'):
        level = int(input("What level of brightness? ")) 
        camera.brightness = level
        # camera.annotate_text_size = 32
        camera.annotate_text = "Brightness: %s" % level
        sleep(delay)
        camera.capture(path + 'Brightness_%s_%s_%s.jpg' %(level,date,time))
        option = input("Choice? ") 
    elif(option == 'contrast'):
        level = int(input("What level of contrast? ")) 
        camera.contrast = level
        camera.annotate_text = "Contrast: %s" % level
        sleep(delay)
        camera.capture(path + 'Contrast_%s_%s_%s.jpg' %(level,date,time))
        option = input("Choice? ")
    elif(option == 'max_res'):
        camera.resolution = (2592, 1944)
        camera.framerate = 15
        camera.annotate_text = "Max Resolution"
        sleep(delay)
        camera.capture(path + 'max_res_%s_%s.jpg' %(date,time))
        option = input("Choice? ") 
    else:
        for effect in camera.IMAGE_EFFECTS:
            if option == effect:
                camera.image_effect = effect
                camera.annotate_text = "Effect: %s" % effect
                sleep(delay)
                camera.capture(path + 'Effect_%s_%s_%s.jpg' %(effect,date,time))
       
        for awb_mode in camera.AWB_MODES:
            if option == awb_mode:
                camera.awb_mode = awb_mode
                camera.annotate_text = "awb_mode: %s" % awb_mode
                sleep(delay)
                camera.capture(path + 'awb_%s_%s_%s".jpg' %(awb_mode,date,time))
     
        for exposure_mode in camera.EXPOSURE_MODES:
            if option == exposure_mode:
                camera.exposure_mode = exposure_mode
                camera.annotate_text = "Exposure_mode: %s" % exposure_mode
                sleep(delay)
                camera.capture(path + 'Exposure_%s_%s_%s.jpg' %(exposure_mode,date,time))
        
        option = input("Choice? ")
        
camera.stop_preview()
camera.close()
