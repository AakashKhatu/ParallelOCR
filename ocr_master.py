import os
from ocr_worker import Worker
from time import time

x = 8

files = os.listdir("sentences")[1:]

start_indexes = [int(len(files)*i/x) for i in range(x)]
indexes = zip(start_indexes, start_indexes[1:])

if __name__ == "__main__":
    start_time = time()
    print("Master started execution")
    for i, (start, end) in enumerate(indexes):
        w = Worker(files[start:end])
        w.start()
    print("Master finished Execution , Completed in : {0} \
        seconds".format(time()-start_time))
