# Picture-Taking-Robot

## Introduction

This project is about turning a robot into a picture taking robot using a Pi Camera Module and the picamera2 Python library. Picamera2 is currently in beta so any issues should be reported to the official repo [here](https://github.com/raspberrypi/picamera2/issues). The way it works is you press a certain key and the robot will take a picture. Note that this only works on Bullseye and newer and cannot work with the Legacy stack enabled.

## Getting started

The desktop versions of Raspberry Pi OS Bullseye and newer contain the picamera2 library by default. The OS images that are Lite or older will require and update and upgrade and then run `sudo apt install -y python3-picamera2`. To not install the GUI dependencies run `sudo apt install -y python3-picamera2 --no-install-recommends`. The code with the `headless` in the file name are used to allow the Robot to move without being tethered to a screen or tethered to VNC.
