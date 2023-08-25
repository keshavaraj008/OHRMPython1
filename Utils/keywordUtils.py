import os
import time

import pandas as pd
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Utils:
    wait = 10

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, att):
        ele = WebDriverWait(self.driver, self.wait).until(expected_conditions.visibility_of_element_located(att))
        ele.click()

    def send_text(self, att, value):
        ele = WebDriverWait(self.driver, self.wait).until(expected_conditions.visibility_of_element_located(att))
        ele.send_keys(value)

    def is_visible(self, att):
        ele = WebDriverWait(self.driver, self.wait).until(expected_conditions.visibility_of_element_located(att))
        return bool(ele)

    def take_screenshot(self):
        filename = str(int(time.time())) + ".png"
        print(filename)
        os.chdir("../")
        filepath = os.path.join("Resources/Screenshots/" + filename)
        self.driver.save_screenshot(filepath)
