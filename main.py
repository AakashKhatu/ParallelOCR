from sklearn.svm import SVC
import matplotlib.pyplot as plt
import os
import cv2
import numpy as np
import pickle

# target = os.listdir("./Screenshots")[1:]
# skip the .gitkeep file
output = open("dataset_pickle", "wb")
dataset = {
    "target": [],
    "data": []
}
img = cv2.imread("./Screenshots/a/Roboto.png", cv2.IMREAD_GRAYSCALE)


def imageprint(img):
    plt.imshow(img, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.show()


for folder in os.listdir("./Screenshots")[1:]:
    for img in os.listdir("./Screenshots/"+folder):
        dataset["data"].append(cv2.imread(
            "./Screenshots/{0}/{1}".format(folder, img), cv2.IMREAD_GRAYSCALE).flatten())
        dataset["target"].append(folder)

pickle.dump(dataset, output)
output.close()
print("completed")
