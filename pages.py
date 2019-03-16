# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys

from Locators import SearchPageLocator
from Locators import ResultPageLocator


class BasePage:

    def __init__(self, driver=None, url=None):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()


class SearchPage(BasePage):

    def __init__(self, driver):
        url = 'https://www.google.com/'
        super().__init__(driver=driver, url=url)

    def search(self, keyword):
        locator = SearchPageLocator.search_box
        search_box = self.driver.find_element(*locator)
        search_box.send_keys(keyword + Keys.ENTER)


class ResultPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def get_result_stats(self):
        locator = ResultPageLocator.result_stats
        result_stats = self.driver.find_element(*locator).text
        return result_stats
