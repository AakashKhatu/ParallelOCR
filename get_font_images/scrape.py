# get screenshot of body tag with font characters
# by loading the template file in browser
from selenium import webdriver

# add chrome driver binary to this path
chrome_path = 'get_font_images/chromedriver.exe'


driver = webdriver.Chrome(chrome_path)
driver.implicitly_wait(10)
with open("get_font_images/test.html", "r") as file:
    html = "\n".join(file.readlines())
name = input("enter font name:")


def getscreenshot(name):
    driver.get("data:text/html;charset=utf-8,"+html.format(name))
    driver.find_element_by_id("box").screenshot("Screenshots/" + name + ".png")
    print("Saved Screenshot of " + name)
