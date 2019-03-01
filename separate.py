import cv2
import numpy as np
from statistics import mean

filename = '1'

start=0
f=True
part = []

img = cv2.imread('processed_files/{0}.png'.format(filename), cv2.IMREAD_GRAYSCALE)
height, width = img.shape[:2]
for i, row in enumerate(img):
    if mean(row) == 255:
        if f is False:
            f = True
            start = i
    else:
        if f is True:
            f = False
            mid = int((start+i)/2)
            part.append(mid)
            cv2.line(img, (0, mid), (width, mid), 0, 1)
cv2.imshow("blank lines", img)
cv2.waitKey(0)
print(part)

for s, e in zip(part, part[1:]):
    print((s, e))