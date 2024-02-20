import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://healthesteem.gr/")
driver.find_element(By.CSS_SELECTOR, "#menu-item-37").click()
time.sleep(2)
driver.find_element((By.LINK_TEXT, "//li[2]/a/h2")).click()
