from sklearn.svm import SVC
import matplotlib.pyplot as plt
import pickle

with open("dataset_pickle", "rb") as d:
    dataset = pickle.load(d)


def imageprint(img):
    plt.imshow(img, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.show()


with open("trained_model", "wb") as m:
    svm = SVC(gamma="scale", probability=True)
    svm.fit(dataset["data"][:-20], dataset["target"][:-20])
    pickle.dump(svm, m)

print(svm.predict(dataset["data"]))
