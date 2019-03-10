from selenium import webdriver
# import logging


class Worker:

    def __init__(self, font_list):
        self.chrome_path = 'get_font_images/chromedriver.exe'
        self.driver = webdriver.Chrome(self.chrome_path)
        self.driver.implicitly_wait(10)

        with open("get_font_images/test.html", "r") as file:
            self.html = "\n".join(file.readlines())

    def get_screenshot(self, name):
        self.driver.get(
            "data:text/html;charset=utf-8,"+self.html.format(name))
        self.driver.find_element_by_id(
            "box").screenshot("Screenshots/" + name + ".png")
        print("Saved Screenshot of " + name)
