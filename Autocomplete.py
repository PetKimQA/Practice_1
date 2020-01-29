from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:/Users/PetruKim/Desktop/Automation/chromedriver.exe")
driver.get("http://formy-project.herokuapp.com/autocomplete")
driver.implicitly_wait(0.5)

autocomplete = driver.find_element_by_xpath("/html/body/div[1]/form/div/div[1]/input")
autocomplete.send_keys("151")

try:
    Ewait = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "pac-item"))
    )
finally:
    auto_result = driver.find_element_by_xpath("/html/body/div[2]/div[2]")
    auto_result.click()

address = driver.find_element_by_id("autocomplete").get_attribute("value")
streetAddress1 = driver.find_element_by_id("street_number").get_attribute("value")
streetAddress2 = driver.find_element_by_id("route").get_attribute("value")
city = driver.find_element_by_id("locality").get_attribute("value")
state = driver.find_element_by_id("administrative_area_level_1").get_attribute("value")
zipCode = driver.find_element_by_id("postal_code").get_attribute("value")
country = driver.find_element_by_id("country").get_attribute("value")

if (
    address, streetAddress1, streetAddress2, city, state, zipCode, country != ""
):
    print("Test Pass")

driver.quit()
