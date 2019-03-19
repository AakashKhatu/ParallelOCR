from sklearn.svm import SVC
import matplotlib.pyplot as plt
import pickle
from random import shuffle
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

with open("dataset_pickle", "rb") as d:
    dataset = pickle.load(d)
logging.info("loaded dataset")

# shuffle dataset without losing labels
combined = list(zip(dataset["data"], dataset["target"]))
shuffle(combined)
dataset["data"], dataset["target"] = zip(*combined)
logging.info("shuffled dataset")


def imageprint(img):
    plt.imshow(img, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.show()


with open("trained_model", "wb") as m:
    svm = SVC(gamma="scale", probability=True)
    svm.fit(dataset["data"], dataset["target"])
    pickle.dump(svm, m)
logging.info("completed training of dataset")
