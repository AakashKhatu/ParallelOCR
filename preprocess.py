import cv2

filename = '1.png'

img = cv2.imread('input_files/{0}'.format(filename), cv2.IMREAD_GRAYSCALE)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
(thresh, img) = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite('processed_files/{0}'.format(filename), img)