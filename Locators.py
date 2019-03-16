# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class SearchPageLocator:

    def __init__(self):
        pass

    search_box = (By.XPATH, '//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')


class ResultPageLocator:

    def __init__(self):
        pass

    result_stats = (By.XPATH, '//*[@id="resultStats"]')
