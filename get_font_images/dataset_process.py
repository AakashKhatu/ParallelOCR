# from time import time
import cv2
import string
import os


def show(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def normalize(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    (thresh, img) = cv2.threshold(
        img, 200, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    img = cv2.bitwise_not(img)
    x, y, w, h = cv2.boundingRect(cv2.findNonZero(img))
    img = img[y:y+h, x:x+w]
    img = cv2.bitwise_not(img)
    img = cv2.resize(img, (16, 16))
    cv2.imwrite(path, img)


for folder in os.listdir("./Screenshots")[1:]:
    for img in os.listdir("./Screenshots/"+folder):
        normalize("./Screenshots/{0}/{1}".format(folder, img))

# # Time Calculation Code
# total = 0
# for letter in string.ascii_letters:
#     start = time()
#     normalize('Screenshots/{0}/Chathura.png'.format(letter))
#     total += time()-start
#     print(time()-start)
# print("average time per font =", total/len(string.ascii_letters), total)

# max average time per letter is 0.003 seconds
