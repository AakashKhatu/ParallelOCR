from Worker import Worker
import json
import time

font_names = json.load(open("get_font_images/font_names.json"))
print(len(font_names))
a = Worker(font_names[0:1])
start = time.time()
a.get_screenshot('Roboto')
mid = time.time()
print("1st font download completed in {0} seconds".format(mid-start))
a.get_screenshot('Antic')
end = time.time()
print("2st font download completed in {0} seconds".format(end-mid))

# Output:
# Saved Screenshot of Roboto
# 1st font download completed in 29.1345317363739 seconds
# Saved Screenshot of Antic
# 2st font download completed in 0.7111871242523193 seconds
