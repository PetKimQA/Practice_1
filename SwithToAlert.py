from selenium import webdriver

driver = webdriver.Firefox("C:/Users/PetruKim/Desktop/Automation")
driver.get("http://formy-project.herokuapp.com/switch-window")

AlertButton = driver.find_element_by_id("alert-button").click()

Alert = driver.switch_to.alert
Alert.accept()

driver.quit()
