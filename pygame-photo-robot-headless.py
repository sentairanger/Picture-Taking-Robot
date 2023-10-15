from datetime import datetime
from picamera2 import Picamera2
import pygame
from gpiozero import Robot, LED

robot = Robot(left=(13, 21), right=(17, 27))
led = LED(25)

screen = pygame.display.set_mode([240,160])

cam = Picamera2()
moment = datetime.now()

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    robot.forward()
                elif event.key == pygame.K_DOWN:
                    robot.backward()
                elif event.key == pygame.K_LEFT:
                    robot.left()
                elif event.key == pygame.K_RIGHT:
                    robot.right()
                elif event.key == pygame.K_p:
                    led.blink(n=1)
                    filename = '/home/torvalds/Pictures/robot_headless_%02d_%02d_%02d.jpg' % (moment.hour, moment.minute, moment.second)
                    cam.start_and_capture_file(filename, delay=0, show_preview=False)
                    print("successful")
                elif event.key == pygame.K_q:
                    print("quitting")
                    pygame.quit()
                    break
            elif event.type == pygame.KEYUP:
                robot.stop()

finally:
    cam.stop()
    cam.close()
