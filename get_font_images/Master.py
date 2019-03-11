from Worker import Worker
import json

font_names = json.load(open("get_font_images/font_names.json"))
total_fonts = len(font_names)
workers = []

# find local minima of this hyperbolic equation
# to get ideal no. of threads for max performance
# running time = init_time * x + total_fonts*time_per_font / x
x = 4

start_indexes = [int(total_fonts*i/x) for i in range(x+1)]
indexes = zip(start_indexes, start_indexes[1:])

if __name__ == "__main__":
    for i, (start, end) in enumerate(indexes):
        w = Worker(font_names[start:end], start, i)
        w.start()
