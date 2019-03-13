from selenium import webdriver
import logging
from multiprocessing import Process
import string


class Worker(Process):

    def __init__(self, font_list, start_index, id):

        super(Worker, self).__init__()

        self.font_list = font_list
        self.start_index = start_index
        self.id = id

        with open("./get_font_images/test.html", "r") as file:
            self.html = "\n".join(file.readlines())

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Started Worker " + str(id))

    def run(self):
        driver_path = r'./get_font_images/geckodriver.exe'
        driver = webdriver.Firefox(executable_path=driver_path)
        driver.implicitly_wait(10)

        logging.basicConfig(
            level=logging.INFO,
            format='%(process)d %(asctime)s - %(levelname)s - %(message)s')

        def get_screenshot(name, i=0):
            driver.get("data:text/html;charset=utf-8,"+self.html.format(name))
            for letter in string.ascii_letters:
                driver.find_element_by_id(letter).screenshot(
                    "Screenshots/{0}/{1}.png".format(letter, name))
            logging.info("Completed Screenshot of " + name)

        for i, font in enumerate(self.font_list):
            get_screenshot(font, i+self.start_index)
        driver.close()
