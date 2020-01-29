from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:/Users/PetruKim/Desktop/Automation/chromedriver.exe")
driver.get("http://formy-project.herokuapp.com/keypress")

try:
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )
finally:
    fullNameField = driver.find_element_by_id("name")
    fullNameField.send_keys("TSKim")

    button = driver.find_element_by_id("button")
    button.click()

driver.close()