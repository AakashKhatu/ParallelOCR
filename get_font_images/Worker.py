from selenium import webdriver
import logging
from multiprocessing import Process


class Worker(Process):

    def __init__(self, font_list, start_index, id):

        super(Worker, self).__init__()

        self.font_list = font_list
        self.start_index = start_index
        self.id = id

        self.chrome_path = 'get_font_images/chromedriver.exe'
        self.driver = webdriver.Chrome(self.chrome_path)
        self.driver.implicitly_wait(10)

        with open("get_font_images/test.html", "r") as file:
            self.html = "\n".join(file.readlines())

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Started Worker " + str(id))

    def get_screenshot(self, name, i=0):
        self.driver.get(
            "data:text/html;charset=utf-8,"+self.html.format(name))
        self.driver.find_element_by_id(
            "box").screenshot("Screenshots/{0}_{1}.png".format(i, name))
        logging.info("Saved Screenshot of " + name)

    def run(self):
        for i, font in enumerate(self.font_list):
            self.get_screenshot(font, i+self.start_index)
