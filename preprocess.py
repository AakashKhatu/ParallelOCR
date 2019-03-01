import cv2
import matplotlib.pyplot as plt

filename = '1.png'

img = cv2.imread('input_files/{0}'.format(filename), cv2.IMREAD_GRAYSCALE)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('processed_files/{0}'.format(filename), img)