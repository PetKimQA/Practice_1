from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/PetruKim/Desktop/Automation/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/bootstrap-dual-list-box-demo.html")
action = ActionChains(driver)

driver.implicitly_wait(2)

# Locators
leftBox = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]/div/ul')
leftItems = leftBox.find_elements_by_class_name('list-group-item')
rightBox = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[3]/div/ul')
rightItems = rightBox.find_elements_by_class_name('list-group-item')
toLeftButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/button[1]')
toRightButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/button[2]')
leftSelectAll = driver.find_element_by_xpath("//*[@id='listhead']/div[2]/div/a")
rightSelectAll = driver.find_element_by_xpath("//*[@id='listhead']/div[1]/div/a")

# Arrays initiate
leftBoxList = []
rightBoxList = []

# Prepare default array
leftBoxList.extend(leftItems)  # adding default li to boxlist arry
rightBoxList.extend(rightItems)  # adding default li to boxlist arry

# Scenario 1 : left to right 1 by 1
try:
    loopRange = range(1, len(leftBoxList) + 1)
    for i in loopRange:
        xpath = '/html/body/div[2]/div/div[2]/div/div[1]/div/ul/li[1]'
        driver.find_element_by_xpath(xpath).click()
        driver.implicitly_wait(0.5)
        toRightButton.click()
        driver.implicitly_wait(0.7)

finally:
    leftResult = []
    leftBox.find_elements_by_class_name('list-group-item').extend(leftResult)
    rightBoxList.extend(rightItems)
    Left_Leng = len(leftResult)
    Right_Leng = len(rightBoxList)

# Scenario 1-1 : left to right test validation
if Left_Leng == 0 and Right_Leng == 10:
    print("Test Pass - all items are moved to right")
else:
    print("Test Failed - Items are not moved")
# Scenario 1-2 : items selection validation
selectedItems = []
rightSelected = rightBox.find_elements_by_xpath("//li[@class='list-group-item active']")
selectedItems.extend(rightSelected)
if len(selectedItems) == 5:
    print("Items were selected")
else:
    print("Selected Items are not detected")

# Scenario 2 :
# Use select all from right box and move to left(Select all -> verify if all were selected -> move left -> verify -> verify if all items are selected
rightSelectAll.click()
driver.implicitly_wait(1)
selectedItems2 = []
selectedItems2.extend(rightBox.find_elements_by_xpath("//li[@class='list-group-item active']"))
if len(selectedItems2) == 10:
    print("All items are selected in right box")
else:
    print("Select All has error in right box")

toLeftButton.click()
leftResult2 = []
leftResult2.extend(leftBox.find_elements_by_xpath("//li[@class='list-group-item active']"))
leftResult2.extend(leftBox.find_elements_by_xpath("//li[@class='list-group-item']"))
Left_Leng2 = len(leftResult2)
rightResult2 = []
rightResult2.extend(rightBox.find_elements_by_xpath("//li[@class='list-group']"))
if Left_Leng2 == 10 and len(rightResult2) == 0:
    print("All items are moved to left")
else:
    print("Test Failed")

driver.quit()
