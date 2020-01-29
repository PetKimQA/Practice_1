from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:/Users/PetruKim/Desktop/Automation/chromedriver.exe")
driver.get("https://openwritings.net/sites/default/files/selenium-test-pages/drag-drop.html")
actionChain = ActionChains(driver)

driver.implicitly_wait(2)
# locators
dragElement = driver.find_element_by_id('draggable')
dropTarget = driver.find_element_by_id('droppable')

# action
actionChain.drag_and_drop(dragElement, dropTarget).perform()

driver.close()


