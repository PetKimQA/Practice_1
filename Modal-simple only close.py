from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:/Users/PetruKim/Desktop/Automation/chromedriver.exe")
driver.get("http://formy-project.herokuapp.com/modal")

driver.find_element_by_id('modal-button').click()
closeButton = driver.find_element_by_id('close-button')
xButton = driver.find_element_by_class_name('close')
okButton = driver.find_element_by_id('ok-button')

try:
    WebDriverWait(driver, 20).until(EC.visibility_of_any_elements_located((By.ID, 'close-button')))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'close-button')))
finally:
    driver.execute_script("arguments[0].click();", closeButton)
