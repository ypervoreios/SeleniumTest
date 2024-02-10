from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

service_obj = Service()
driver = webdriver.Firefox(service=service_obj)
driver.maximize_window()
driver.get("https://healthesteem.gr/contact/")
driver.find_element(By.ID, "wpforms-43-field_0").send_keys("John Doe")
driver.find_element(By.ID, "wpforms-43-field_3").send_keys(6971801725)
driver.find_element(By.ID, "wpforms-43-field_1").send_keys("example@gmail.com")
driver.find_element(By.ID, "wpforms-43-field_2").send_keys("Bla bla bla bla bla")
driver.find_element(By.ID, "wpforms-43-field_4_1").click()
#WebDriverWait(driver, 10).until(ec.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
#WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
driver.find_element(By.CLASS_NAME, "wpforms-submit").click()
message = driver.find_element(By.ID, "wpforms-confirmation-43").text
print(message)
assert "Thanks" in message