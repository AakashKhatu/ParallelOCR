# get screenshot of body tag with font characters by loading the template file in browser
from selenium import webdriver

driver = webdriver.Chrome('Font Downloader/chromedriver.exe')
driver.implicitly_wait(10)
with open("Font Downloader/test.html", "r") as file:
    html = "\n".join(file.readlines())
name = input("enter font name:")
while name is not "exit":
    driver.get("data:text/html;charset=utf-8,"+html.format(name))
    driver.find_element_by_id("box").screenshot("Screenshots\\"+ name +".png")
    print("Saved Screenshot of " + name)
    name = input("enter font name:")
