# Colour Detection with OpenCV and Numpy

This script uses `OpenCV` and `Numpy` to detect colors and separates them in an image.

An Argument Parser has been used to construct usable instructions. RGB boundaries for different colors are used to match borderline boundaries to detect colors. An **OpenCV Bitwise_AND mask** is used to mask the numpy arrays containing the RGB values and match it with the original image to detect colours.

---

**Environment Setup**

`$ pip install opencv2`
`$ pip install numpy`

---

**Usage Instructions**

`$ python detect_color.py --image imagename.jpg`

---

The program can be used to help color blind people recognize colours.

**Future Development**

Mounting a camera on a pair of glasses and helping color blind people differentiate colors in **real life** by running this script on the backend of the camera (eg. pi camera)
