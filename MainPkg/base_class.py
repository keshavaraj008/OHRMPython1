import os

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def datafile():
    # os.chdir('../')
    data = pd.read_csv("Resources/datafile.csv", index_col='Case', header=0)
    df1 = pd.DataFrame(data)
    return df1


class Browser:

    data = []

    @staticmethod
    def collect_data():
        Browser.data = datafile()

    @staticmethod
    def select_browser():
        return "Chrome"

    @staticmethod
    def chrome_driver():
        service = ChromeService(ChromeDriverManager.install(ChromeDriverManager()))
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    @staticmethod
    def firefox_driver():
        service = Service(GeckoDriverManager.install(GeckoDriverManager()))
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
        return driver

    @staticmethod
    def fetch_data(row, column):
        data = Browser.data
        df1 = pd.DataFrame(data)
        d1 = df1.loc[row, column]
        print(d1)
        return d1


