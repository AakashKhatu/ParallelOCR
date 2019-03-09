import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
import time

start = time.time()
digits = datasets.load_digits()
clf = svm.SVC()
clf = svm.SVC(gamma=0.001, C=100)
X,y = digits.data[:-20], digits.target[:-20]
clf.fit(X,y)
print(clf.predict(digits.data[-11:-2]))
plt.imshow(digits.images[-8], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

end = time.time()
print("done", end-start)