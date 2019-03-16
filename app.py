from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.google.com/')

search_box = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
search_box.send_keys('ブラウザ自動化ツール' + Keys.ENTER)

result_stats = driver.find_element_by_xpath('//*[@id="resultStats"]').text
print(result_stats)

sleep(1)
driver.quit()
