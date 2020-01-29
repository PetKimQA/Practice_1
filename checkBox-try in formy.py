import self as self
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:/Users/PetruKim/Desktop/Automation/chromedriver.exe")
driver.get("http://formy-project.herokuapp.com/checkbox")

#locators
cb1 = driver.find_element_by_xpath('//*[@id="checkbox-1"]')
cb2 = driver.find_element_by_xpath('//*[@id="checkbox-2"]')
print("found locators")

#actions
cb1_presence = cb1.is_enabled()
cb2_presence = cb2.is_enabled()
cb1_validation = cb1.is_selected()
cb2_validation = cb2.is_selected()

print("defined validation")

if cb1_validation and cb1_presence is True:
    print("cb1 is already checked")
else:
    ActionChains(driver).move_to_element(cb1).double_click().send_keys(Keys.SPACE)
    print("cb1 was not checked, now we did")





