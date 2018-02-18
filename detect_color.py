# USAGE
# python detect_color.py --image pokemon_games.png

# import the necessary packages
def colour_detection():

	import numpy as np
	import argparse
	import cv2

	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", help = "path to the image")
	args = vars(ap.parse_args())

	# load the image
	image = cv2.imread(args["image"])

	# define the list of boundaries
	boundariesblue = [
		([86, 31, 4], [220, 88, 50]),
		([17, 15, 100], [50, 56, 200]),
		([25, 146, 190], [62, 174, 250]),
		([103, 86, 65], [145, 133, 128])
	]

	boundariesred = [
			([17, 15, 100], [50, 56, 200]),
			([86, 31, 4], [220, 88, 50]),
			([25, 146, 190], [62, 174, 250]),
			([103, 86, 65], [145, 133, 128])
	]

	boundariesyellow = [
			([25, 146, 190], [62, 174, 250]),
			([86, 31, 4], [220, 88, 50]),
			([17, 15, 100], [50, 56, 200]),
			([103, 86, 65], [145, 133, 128])
	]

	boundariesgrey = [
			([103, 86, 65], [145, 133, 128]),
			([86, 31, 4], [220, 88, 50]),
			([17, 15, 100], [50, 56, 200]),
			([25, 146, 190], [62, 174, 250]),
	]

	user = raw_input("Which color do you want to detect?")
	# loop over the boundaries
	if (user=="RED" or user=="red" or user=="Red" or user=="R"):

		for (lower, upper) in boundariesred:
			# create NumPy arrays from the boundaries
			lower = np.array(lower, dtype = "uint8")
			upper = np.array(upper, dtype = "uint8")

			# find the colors within the specified boundaries and apply
			# the mask
			mask = cv2.inRange(image, lower, upper)
			output = cv2.bitwise_and(image, image, mask = mask)

			# show the images
			cv2.imshow("images", np.hstack([image, output]))
			cv2.waitKey(0)
			ans1 = raw_input("Want to try again?")
			if (ans1=="Y" or ans1=="Yes"):
				colour_detection()
			else:
				print "Thank you for using"

	elif (user=="BLUE" or user=="blue" or user=="Blue" or user=="B"):

		for (lower, upper) in boundariesblue:
			# create NumPy arrays from the boundaries
			lower = np.array(lower, dtype = "uint8")
			upper = np.array(upper, dtype = "uint8")

			# find the colors within the specified boundaries and apply
			# the mask
			mask = cv2.inRange(image, lower, upper)
			output = cv2.bitwise_and(image, image, mask = mask)

			# show the images
			cv2.imshow("images", np.hstack([image, output]))
			cv2.waitKey(0)

	elif (user=="YELLOW" or user=="yellow" or user=="Yellow" or user=="Y"):

		for (lower, upper) in boundariesyellow:
			# create NumPy arrays from the boundaries
			lower = np.array(lower, dtype = "uint8")
			upper = np.array(upper, dtype = "uint8")

			# find the colors within the specified boundaries and apply
			# the mask
			mask = cv2.inRange(image, lower, upper)
			output = cv2.bitwise_and(image, image, mask = mask)

			# show the images
			cv2.imshow("images", np.hstack([image, output]))
			cv2.waitKey(0)

	elif (user=="GREY" or user=="grey" or user=="Grey" or user=="Gr"):

		for (lower, upper) in boundariesgrey:
			# create NumPy arrays from the boundaries
			lower = np.array(lower, dtype = "uint8")
			upper = np.array(upper, dtype = "uint8")

			# find the colors within the specified boundaries and apply
			# the mask
			mask = cv2.inRange(image, lower, upper)
			output = cv2.bitwise_and(image, image, mask = mask)

			# show the images
			cv2.imshow("images", np.hstack([image, output]))
			cv2.waitKey(0)

	else:

		print "Invalid Colour. Colour detection not supported"
		ans = raw_input("Want to try again?")
		if (ans=="Y" or ans=="Yes"):
			colour_detection()
		else:
			print "Thanks!"

colour_detection()
