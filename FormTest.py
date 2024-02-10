from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://healthesteem.gr/contact/")
driver.find_element(By.ID, "wpforms-43-field_0").send_keys("John Doe")
driver.find_element(By.ID, "wpforms-43-field_3").send_keys(6970000000)
driver.find_element(By.ID, "wpforms-43-field_1").send_keys("example@gmail.com")
driver.find_element(By.ID, "wpforms-43-field_2").send_keys("Bla bla bla bla bla")
driver.find_element(By.ID, "wpforms-43-field_4_1").click()
driver.find_element(By.XPATH, "//button[.='Αποστολή']").click()
message = driver.find_element(By.ID, "wpforms-confirmation-43").text
print(message)
assert "Thanks" in message
