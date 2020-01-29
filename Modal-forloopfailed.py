from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:/Users/PetruKim/Desktop/Automation/chromedriver.exe")
actionChains = ActionChains(driver)
driver.get("http://formy-project.herokuapp.com/modal")

modalButton = driver.find_element_by_id('modal-button')
modalButton.click()
# closeButton = driver.find_element_by_class_name('btn btn-info')
# xButton = driver.find_element_by_class_name('close')
# okButton = driver.find_element_by_class_name('btn btn-primary')

locatorList = ['btn btn-info', 'close', 'btn btn-primary']
for i in locatorList:
    try:
        WebDriverWait(driver, 20).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, i)))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(By.CLASS_NAME, i))
    finally:  # got stuck here
        driver.find_element_by_class_name('close-button').click()
        WebDriverWait(driver, 20).until(EC.visibility_of_any_elements_located((By.ID, 'modal-button')))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'modal-button')))
        modalButton.click()

driver.quit()

