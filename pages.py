# -*- coding: utf-8 -*-

from Locators import SearchPageLocator
from Locators import ResultPageLocator

from elements import InputElement


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

    @property
    def search_box(self):
        locator = SearchPageLocator.search_box
        return InputElement(
            driver=self.driver,
            locator=locator
        )


class ResultPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def get_result_stats(self):
        locator = ResultPageLocator.result_stats
        result_stats = self.driver.find_element(*locator).text
        return result_stats
