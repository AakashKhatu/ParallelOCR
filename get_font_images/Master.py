from Worker import Worker
import json
from time import time
from string import ascii_letters
from os import makedirs

for letter in ascii_letters:
    try:
        makedirs("./Screenshots/"+letter)
    except FileExistsError:
        pass

font_names = json.load(open("get_font_images/font_names.json"))
total_fonts = len(font_names)
workers = []

# read benchmark.md
x = 7

start_indexes = [int(total_fonts*i/x) for i in range(x+1)]
indexes = zip(start_indexes, start_indexes[1:])

if __name__ == "__main__":
    start_time = time()
    print("Master started execution")
    for i, (start, end) in enumerate(indexes):
        w = Worker(font_names[start:end], start, i)
        workers.append(w)
        w.start()
    for w in workers:
        w.join()
    print("Master finished Execution , Completed in : {0} \
        seconds".format(time()-start_time))
