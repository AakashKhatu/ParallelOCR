# single instance of multi threaded scraper
# implemented in master and worker modules
# Used for calculating time equation contants

# get screenshot of body tag with font characters
# by loading the template file in browser
from selenium import webdriver
import string
import os
from time import time

# create directory structure for letters
for letter in string.ascii_letters:
    try:
        os.makedirs("./Screenshots/"+letter)
    except FileExistsError:
        pass

ct = time()
print("started driver")
# add geckodriver binary to this path
driver_path = r'./get_font_images/geckodriver.exe'

driver = webdriver.Firefox(executable_path=driver_path)
driver.implicitly_wait(10)
with open("get_font_images/test.html", "r") as file:
    html = "\n".join(file.readlines())
print("driver initialized", time()-ct)
ct = time()


def getscreenshot(name):
    global ct
    driver.get("data:text/html;charset=utf-8,"+html.format(name))
    print("page loaded in ", time()-ct)
    ct = time()
    for letter in string.ascii_letters:
        driver.find_element_by_id(letter).screenshot(
            "Screenshots/{0}/{1}.png".format(letter, name))
    print("completed in ", time()-ct)


getscreenshot('Roboto')
ct = time()
getscreenshot('Raleway')
ct = time()
getscreenshot('Sniglet')
