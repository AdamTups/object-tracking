"""
A utility to define the initial bounding box for the object being tracked by an
object tracking algorithm.

Execute using the following command:

    python bounding_box_finder.py <PATH TO VIDEO FILE>

Author: Adam Tupper
Date: 26/09/18
"""
import sys
import cv2
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def main():
    print("Dependency Info:")
    print("Python Version: {}".format(sys.version.split('|')[0]))
    print("OpenCV Version: {}".format(cv2.__version__))
    print("Matplotlib Version: {}".format(matplotlib.__version__))
    print()

    if len(sys.argv) < 2:
        print("No video file path given.")
        quit()
    
    VIDEO_PATH = sys.argv[1]
    video = cv2.VideoCapture(VIDEO_PATH)

    if not video.isOpened():
        print("Could not load video.")
        quit()
    else:
        print("Video loaded!")
        print()

    # Read the first video frame
    read_ok, frame = video.read()

    # Define initial bounding box
    bbox = (0, 0, 0, 0)

    # Uncomment the line below to select a different bounding box
    bbox = cv2.selectROI(frame, False)

    print("Bounding box:", bbox)

if __name__ == "__main__":
    main()