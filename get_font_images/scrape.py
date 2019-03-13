# single instance of multi threaded scraper
# implemented in master and worker modules

# get screenshot of body tag with font characters
# by loading the template file in browser
from selenium import webdriver
import string
import os

# create directory structure for letters
for letter in string.ascii_letters:
    try:
        os.makedirs("./Screenshots/"+letter)
    except FileExistsError:
        pass


# add geckodriver binary to this path
driver_path = r'./get_font_images/geckodriver.exe'

driver = webdriver.Firefox(executable_path=driver_path)
driver.set_window_size(1080, 500)
driver.implicitly_wait(10)
with open("get_font_images/test.html", "r") as file:
    html = "\n".join(file.readlines())


def getscreenshot(name):
    driver.get("data:text/html;charset=utf-8,"+html.format(name))
    for letter in string.ascii_letters:
        driver.find_element_by_id(letter).screenshot(
            "Screenshots/{0}/{1}.png".format(letter, name))
