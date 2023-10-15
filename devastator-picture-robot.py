#import libraries
import curses
from gpiozero import Robot, LED
import os
from picamera2 import Picamera2, Preview
from time import strftime


#set variable for robot and eye
devastator_robot = Robot(left=(13, 21), right=(17, 27))
eye = LED(25)

# Define the camera
cam = Picamera2()
cam.start_preview(Preview.DRM)
cam.start()

# Blink eye 2 times to ensure the code is running correctly
eye.blink(n=2)

#setup your actions
actions = {
    curses.KEY_UP:    devastator_robot.forward,
    curses.KEY_DOWN:  devastator_robot.backward,
    curses.KEY_LEFT:  devastator_robot.left,
    curses.KEY_RIGHT: devastator_robot.right,

    }

#main curses function
def main(window):
    next_key = None
    while True:
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            #when key is pressed
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            #when key is released
            devastator_robot.stop()
        if key == ord('q'):
            print("quitting")
            break #quit the module
        if key == ord('s'):
            os.system('sudo shutdown now') #shutdown the pi
        if key == ord('p'):
            eye.blink(n=1)
            filename = strftime("%Y%m%d-%H%M%S") + '.png'
            cam.capture_file(filename, format="png", wait=None)
            print(f"\rCaptured {filename} succesfully")

curses.wrapper(main)
devastator_robot.stop()
cam.stop_preview()
cam.stop()
cam.close()
