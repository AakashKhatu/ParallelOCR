from selenium import webdriver

driver = webdriver.Chrome('Font Downloader/chromedriver.exe')
driver.implicitly_wait(10)
with open("Font Downloader/test.html", "r") as file:
    html = "\n".join(file.readlines())
name = "Ubuntu"
driver.get("data:text/html;charset=utf-8,"+html.format(name))
driver.find_element_by_id("box").screenshot("Screenshots\\"+ name +".png")
print("savedss")