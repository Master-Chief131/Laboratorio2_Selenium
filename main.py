from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")
text_box = driver.find_element(by=By.ID, value="twotabsearchtextbox")
submit_button = driver.find_element(by=By.ID, value="nav-search-submit-button")
text_box.send_keys("HP Pavilion azul")
submit_button.click()
item = driver.find_element(by=By.CLASS_NAME, value="s-image")
item.click()
amount_dropdown = driver.find_element(by=By.CLASS_NAME, value="a-button-inner")
amount_dropdown.click()
amount = driver.find_element(by=By.ID, value="quantity_1")
amount.click()
addItem = driver.find_element(by=By.ID, value="add-to-cart-button")
addItem.click()
time.sleep(5)
close = driver.find_element(by=By.ID, value="attach-close_sideSheet-link")
close.click()
seeItem = driver.find_element(by=By.ID, value="nav-cart-count-container")
seeItem.click()

time.sleep(20)
driver.close()
