import cv2
import numpy as np

image = cv2.imread('resim1.jpg')
red_channel, green_channel, blue_channel = cv2.split(image)

cv2.imshow('Red', red_channel)
cv2.waitKey(0)
cv2.imshow('Green', green_channel)
cv2.waitKey(0)
cv2.imshow('Blue', blue_channel)
cv2.waitKey(0)


no_green_image = cv2.merge((blue_channel,np.zeros_like(green_channel),red_channel))
cv2.imshow('No green image', no_green_image)
cv2.waitKey(0)

original_coloured_image = cv2.merge((blue_channel, green_channel, red_channel))
cv2.imshow('Original image', original_coloured_image)
cv2.waitKey(0)
cv2.destroyAllWindows()