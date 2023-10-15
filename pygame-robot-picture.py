from time import strftime
from picamera2 import Picamera2, Preview
import pygame
from gpiozero import Robot, LED

robot = Robot(left=(13, 21), right=(17, 27))
led = LED(25)

screen = pygame.display.set_mode([240,160])

cam = Picamera2()
cam.start_preview(Preview.DRM)
cam.start()

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
                    filename = strftime("%Y%m%d-%H%M%S") + '.png'
                    cam.capture_file(filename, format="png", wait=None)
                    print(f"\rCaptured {filename} succesfully")
                elif event.key == pygame.K_q:
                    print("quitting")
                    pygame.quit()
                    break
            elif event.type == pygame.KEYUP:
                robot.stop()

finally:
    cam.stop_preview()
    cam.stop()
    cam.close()