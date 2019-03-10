import cv2
import numpy as np
from statistics import mean

filename = '1'
# Value above which a line is considered to be blank 255 for pure white
threshold = 255

start=0
# flag for measuring start and end of blank horizontal space
f=True
part = []
img = cv2.imread('processed_files/{0}.png'.format(filename), cv2.IMREAD_GRAYSCALE)
height, width = img.shape[:2]


for i, row in enumerate(img):
    if mean(row) >= threshold:
        if f is False:
            # mark start of blank space
            f = True
            start = i
    else:
        if f is True:
            # mark end of blank space
            f = False
            # calculate middle of blank space and store y value
            mid = int((start+i)/2)
            part.append(mid)
            cv2.line(img, (0, mid), (width, mid), 0, 1)
# for representation purposes only
cv2.imwrite("processed_files/{0}_lines.png".format(filename), img)
cv2.waitKey(0)
# crop and save file into strips
for i, (s, e) in enumerate(zip(part, part[1:])): # zip to make array of tuples of (start, end)
    cv2.imwrite("sentences/{0}_{1}.png".format(filename, i), img[s:e])
# if image dosent start or end with a blank space , 1st and last line is lost