from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep
import numpy as np 
import cv2

camera = PiCamera()
camera.resolution = (640, 480)
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
sleep(0.1)

for i in range(100):
	# grab an image from the camera
	camera.rotation = 180
	camera.capture(rawCapture, format="bgr")
	image = rawCapture.array

	# display the image on screen and wait for a keypress
	cv2.imshow("Image", image)
	cv2.waitKey(1)