from selenium import webdriver

driver = webdriver.Chrome("C:/Users/PetruKim/Desktop/Automation/chromedriver.exe")
driver.get("http://formy-project.herokuapp.com/scroll")
driver.implicitly_wait(0.5)

fullName = driver.find_element_by_id("name")
fullName.location_once_scrolled_into_view
fullName.send_keys("TestKim")

dateField = driver.find_element_by_id("date")
dateField.send_keys("12/24/2019")

driver.quit()
