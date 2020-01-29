from selenium import webdriver


driver = webdriver.Chrome("C:/Users/PetruKim/Desktop/Automation/chromedriver.exe")
driver.get("http://formy-project.herokuapp.com/switch-window")
driver.implicitly_wait(0.5)

newTab = driver.find_element_by_id("new-tab-button")
newTab.click()

handles = driver.window_handles
size = len(handles)
parent_handle = driver.current_window_handle
for x in range(size):
    if handles[x] != parent_handle:
        driver.switch_to.window(handles[x])
        driver.close()

driver.switch_to.window(parent_handle)

driver.quit()


