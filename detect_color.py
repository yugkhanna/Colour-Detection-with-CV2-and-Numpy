""" USAGE
python detect_color.py --image imagename.jpg """

import numpy as np
import cv2
import argparse

def detect_color():

	# constructing argument parser and parsing the arguments
	argument_p = argparse.ArgumentParser()
	argument_p.add_argument("-i", "--image", help = "path to the image")
	args = vars(argument_p.parse_args())

	# load the image
	image = cv2.imread(args["image"])

	boundaries_blue = [
		([86, 31, 4], [220, 88, 50]),
		([17, 15, 100], [50, 56, 200]),
		([25, 146, 190], [62, 174, 250]),
		([103, 86, 65], [145, 133, 128])
	]

	boundaries_red = [
			([17, 15, 100], [50, 56, 200]),
			([86, 31, 4], [220, 88, 50]),
			([25, 146, 190], [62, 174, 250]),
			([103, 86, 65], [145, 133, 128])
	]

	boundaries_yellow = [
			([25, 146, 190], [62, 174, 250]),
			([86, 31, 4], [220, 88, 50]),
			([17, 15, 100], [50, 56, 200]),
			([103, 86, 65], [145, 133, 128])
	]

	boundaries_grey = [
			([103, 86, 65], [145, 133, 128]),
			([86, 31, 4], [220, 88, 50]),
			([17, 15, 100], [50, 56, 200]),
			([25, 146, 190], [62, 174, 250]),
	]

	user = input("Which color do you want to detect?")
	# loop over the boundaries
	if (user.islower()=="red" or user.isupper()=="RED"):
		for (lower_boundary, upper_boundary) in boundaries_red:

			lower_boundary = np.array(lower_boundary, dtype = "uint8")
			upper_boundary = np.array(upper_boundary, dtype = "uint8")

			mask = cv2.inRange(image, lower_boundary, upper_boundary)
			output = cv2.bitwise_and(image, image, mask = mask)

			cv2.imshow("images", np.hstack([image, output]))
			cv2.waitKey(0)
			answer = raw_input("Want to try again?")
			if (answer=="Y" or answer=="Yes"):
				detect_color()
			else:
				print "Thank you for using"

	elif (user.islower()=="blue" or user.isupper()=="BLUE"):

		for (lower_boundary, upper_boundary) in boundaries_blue:
			# create NumPy arrays from the boundaries
			lower_boundary = np.array(lower_boundary, dtype = "uint8")
			upper_boundary = np.array(upper_boundary, dtype = "uint8")

			# find the colors within the specified boundaries and apply
			# the mask
			mask = cv2.inRange(image, lower_boundary, upper_boundary)
			output = cv2.bitwise_and(image, image, mask = mask)

			# show the images
			cv2.imshow("images", np.hstack([image, output]))
			cv2.waitKey(0)
			answer = raw_input("Want to try again?")
			if (answer=="Y" or answer=="Yes"):
				detect_color()
			else:
				print "Thank you for using"

	elif (user.islower()=="yellow" or user.isupper()=="YELLOW"):

		for (lower_boundary, upper_boundary) in boundaries_yellow:
			# create NumPy arrays from the boundaries
			lower_boundary = np.array(lower_boundary, dtype = "uint8")
			upper_boundary = np.array(upper_boundary, dtype = "uint8")

			# find the colors within the specified boundaries and apply
			# the mask
			mask = cv2.inRange(image, lower_boundary, upper_boundary)
			output = cv2.bitwise_and(image, image, mask = mask)

			# show the images
			cv2.imshow("images", np.hstack([image, output]))
			cv2.waitKey(0)
			answer = raw_input("Want to try again?")
			if (answer=="Y" or answer=="Yes"):
				detect_color()
			else:
				print "Thank you for using"

	elif (user.islower()=="grey" or user.isupper()=="GREY"):

		for (lower_boundary, upper_boundary) in boundaries_grey:
			# create NumPy arrays from the boundaries
			lower_boundary = np.array(lower_boundary, dtype = "uint8")
			upper_boundary = np.array(upper_boundary, dtype = "uint8")

			# find the colors within the specified boundaries and apply
			# the mask
			mask = cv2.inRange(image, lower_boundary, upper_boundary)
			output = cv2.bitwise_and(image, image, mask = mask)

			# show the images
			cv2.imshow("images", np.hstack([image, output]))
			cv2.waitKey(0)
			answer = raw_input("Want to try again?")
			if (answer=="Y" or answer=="Yes"):
				detect_color()
			else:
				print "Thank you for using"

	else:

		print "Invalid Colour. Colour detection not supported"
		ans = input("Want to try again? Y/N")
		if (ans.isupper()=="Y" or ans.islower()=="y"):
			detect_color()
		else:
			print "Thanks!"

detect_color()
