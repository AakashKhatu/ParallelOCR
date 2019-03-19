import cv2
from statistics import mean
import matplotlib.pyplot as plt
import pickle
import logging
from multiprocessing import Process


class Worker(Process):

    def __init__(self, filenames):
        super(Worker, self).__init__()
        self.model = pickle.load(open("trained_model", "rb"))
        self.filenames = filenames

    def imageprint(self, img):
        plt.imshow(img, cmap=plt.cm.gray_r, interpolation='nearest')
        plt.show()

    def normalize(self, img):
        (thresh, img) = cv2.threshold(
            img, 200, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        img = cv2.bitwise_not(img)
        x, y, w, h = cv2.boundingRect(cv2.findNonZero(img))
        img = img[y:y+h, x:x+w]
        img = cv2.bitwise_not(img)
        img = cv2.resize(img, (16, 16))
        img = cv2.normalize(img, 0, 255, cv2.NORM_MINMAX)
        return img

    def run(self):
        for fn in self.filenames:
            self.line = cv2.imread("sentences/"+fn, cv2.IMREAD_GRAYSCALE)
            height, width = self.line.shape[:2]
            # flag value for detecting filled pixels
            f = False
            # threshold for detecting filled pixels
            thresh = 247

            self.letters = []
            start = 0
            # read separate_lines.py for comments
            for i, col in enumerate(self.line.T):
                if mean(col) <= thresh:
                    if f is False:
                        f = True
                        start = i
                else:
                    if f is True:
                        f = False
                        self.letters.append((start, i))

            logging.basicConfig(
                level=logging.INFO,
                format='%(process)d-%(asctime)s-%(levelname)s - %(message)s')

            def p(x):
                img = self.normalize(
                    self.line[:, self.letters[x][0]:self.letters[x][1]])
                return self.model.predict([img.flatten()])

            a = "".join([p(i)[0] for i in range(len(self.letters))])
            open("output_text/"+fn+".txt", "a+").write(fn+" "+a)
            logging.info("worker completed file : "+fn)
