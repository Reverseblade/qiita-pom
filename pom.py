from time import sleep

from selenium import webdriver

from pages import SearchPage
from pages import ResultPage

driver = webdriver.Chrome('./chromedriver')

search_page = SearchPage(driver)
search_page.open()
search_page.search_box.search('ブラウザ自動化ツール')

result_page = ResultPage(search_page.driver)
print(result_page.get_result_stats())

sleep(1)
result_page.close()
