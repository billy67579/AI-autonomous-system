# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
cam = cv2.VideoCapture("/home/billy/Test/Videos/cl.mp4.mp4")

try:
	# creating a folder named data
	if not os.path.exists('data'):
		os.makedirs('data')

# if not created then raise error
except OSError:
	print ('Error: Creating directory of data')

# frame
currentframe = 0
skipframe = 2

while(True):
	
	# reading from frame
	ret,frame = cam.read()

	if not ret:
		break
	# increasing counter so that it will
	# show how many frames are created
	currentframe += 1

	#checking if the frame should be skipped or not
	if currentframe % skipframe != 0:
		continue
	
	# if video is still left continue creating images
	name = '/home/billy/Test/data/lane' + str(currentframe) + '.jpg'
	print ('Creating...' + name)

	# writing the extracted images
	cv2.imwrite(name, frame)

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
